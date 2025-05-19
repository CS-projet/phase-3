import time
import os
from aes import aes_encrypt, aes_decrypt
from rsa import generate_rsa_keys, rsa_encrypt, rsa_decrypt
from ecc import generate_ecc_keys, derive_shared_key, ecc_encrypt, ecc_decrypt
from ai_optimizer import get_best_encryption_method

def load_test_data(size_kb):
    return os.urandom(size_kb * 1024)

def benchmark(size_kb=1024, sensitive=False):
    data = load_test_data(size_kb)
    method = get_best_encryption_method(size_kb, sensitive)
    print(f"Using: {method} for {size_kb}KB")

    if method == "AES":
        start = time.time()
        enc, key = aes_encrypt(data)
        dec = aes_decrypt(enc, key)
        end = time.time()
    elif method == "RSA":
        priv, pub = generate_rsa_keys()
        start = time.time()
        enc = rsa_encrypt(data[:190], pub)  # RSA max is ~190 bytes
        dec = rsa_decrypt(enc, priv)
        end = time.time()
    elif method == "ECC":
        priv, pub = generate_ecc_keys()
        peer_priv, peer_pub = generate_ecc_keys()
        shared_key = derive_shared_key(priv, peer_pub)
        start = time.time()
        enc = ecc_encrypt(data, shared_key)
        dec = ecc_decrypt(enc, shared_key)
        end = time.time()
    else:
        print("Unknown method.")
        return

    print(f"Time taken: {end - start:.4f} sec")
    print("Decryption successful:", dec[:10] == data[:10])

if __name__ == "__main__":
    benchmark(240, sensitive=False)
