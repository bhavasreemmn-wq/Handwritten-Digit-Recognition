import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train, X_test = X_train / 255.0, X_test / 255.0
X_train = np.expand_dims(X_train, axis=-1)
X_test = np.expand_dims(X_test, axis=-1)
print(f"Training data shape: {X_train.shape}")
print(f"Test data shape: {X_test.shape}\n")
model = models.Sequential([
    layers.Input(shape=(28, 28, 1)), 
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
])
model.summary()
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
print("\n### Starting Model Training ###")
model.fit(X_train, y_train, epochs=5, batch_size=64, validation_split=0.1)
print("\n### Evaluating on Test Dataset ###")
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print(f"\nTest Dataset Accuracy: {test_acc * 100:.2f}%")
