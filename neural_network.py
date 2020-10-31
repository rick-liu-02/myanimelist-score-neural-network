import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
import numpy as np

x = np.genfromtxt("data/x.csv", dtype=np.float32, delimiter=",")
y = np.genfromtxt("data/y.csv", dtype=np.float32, delimiter=",")

x_train = x[:10000]
y_train = y[:10000]

x_test = x[10000:]
y_test = y[10000:]

model = keras.Sequential()
model.add(keras.Input(shape=(117)))
model.add(layers.Dense(128, activation="relu"))
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(1))

print(model.summary())

model.compile(
    loss=keras.losses.MeanSquaredError(),
    optimizer=keras.optimizers.Adam(lr=0.001),
    metrics=["accuracy", "mean_squared_error", "mean_absolute_error"]
)

model.fit(x_train, y_train, batch_size=10, epochs=100, verbose=2)
model.evaluate(x_test, y_test, batch_size=10, verbose=2)

models.save_model(model, "model")