import numpy as np
import tensorflow as tf
import joblib


model = tf.keras.models.load_model("model.keras")
label_encoder = joblib.load("label_encoder.pkl")


TRAIN_MAX_SIZE = 14976
TRAIN_MAX_SENSITIVE = 1

def get_best_encryption_method(data_size_kb, is_sensitive):

    input_data = np.array([[data_size_kb / TRAIN_MAX_SIZE, is_sensitive / TRAIN_MAX_SENSITIVE]])

    prediction = model.predict(input_data, verbose=0)
    predicted_index = np.argmax(prediction)
    return label_encoder.inverse_transform([predicted_index])[0]

