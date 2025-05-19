import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import r2_score


df = pd.read_csv("encryption_dataset.csv")


label_encoder = LabelEncoder()
df["method_label"] = label_encoder.fit_transform(df["method"])  # AES=0, ECC=1, RSA=2


X = df[["size_kb", "sensitive"]].values
y = to_categorical(df["method_label"].values, num_classes=3)


X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)


X_train = X_train / np.max(X_train, axis=0)
X_val = X_val / np.max(X_val, axis=0)


model = Sequential([
    Dense(16, activation="relu", input_shape=(2,)),
    Dense(16, activation="relu"),
    Dense(3, activation="softmax")  # 3 classes: AES, RSA, ECC
])

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])


history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_val, y_val))



model.save("model.keras")
joblib.dump(label_encoder, "label_encoder.pkl")



print("✅ TensorFlow model trained and saved with curves.")
