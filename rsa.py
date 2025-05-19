from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_rsa_keys():
    key = RSA.generate(2048)
    return key, key.publickey()

def rsa_encrypt(data: bytes, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    return cipher.encrypt(data)

def rsa_decrypt(ciphertext: bytes, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    return cipher.decrypt(ciphertext)
