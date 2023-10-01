import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, LSTM, Embedding

# Cargar y preprocesar datos
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocesar para MLP y CNN
train_images_mlp_cnn = train_images.reshape((60000, 28 * 28)).astype('float32') / 255
test_images_mlp_cnn = test_images.reshape((10000, 28 * 28)).astype('float32') / 255

# Preprocesar para RNN
train_images_rnn = train_images.astype('float32') / 255
test_images_rnn = test_images.astype('float32') / 255

# One-hot encoding de las etiquetas
train_labels = tf.keras.utils.to_categorical(train_labels)
test_labels = tf.keras.utils.to_categorical(test_labels)

# Definir modelos
# 1. MLP
model_mlp = Sequential([
    Dense(128, activation='relu', input_shape=(784,)),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# 2. CNN
model_cnn = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# 3. RNN
model_rnn = Sequential([
    LSTM(128, return_sequences=True, input_shape=(28, 28)),
    LSTM(128),
    Dense(10, activation='softmax')
])

# Compilar modelos
model_mlp.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model_cnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model_rnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar modelos
model_mlp.fit(train_images_mlp_cnn, train_labels, epochs=5, batch_size=64)
model_cnn.fit(train_images_mlp_cnn.reshape(60000, 28, 28, 1), train_labels, epochs=5, batch_size=64)
model_rnn.fit(train_images_rnn, train_labels, epochs=5, batch_size=64)

# Evaluar modelos
test_loss_mlp, test_acc_mlp = model_mlp.evaluate(test_images_mlp_cnn, test_labels)
test_loss_cnn, test_acc_cnn = model_cnn.evaluate(test_images_mlp_cnn.reshape(10000, 28, 28, 1), test_labels)
test_loss_rnn, test_acc_rnn = model_rnn.evaluate(test_images_rnn, test_labels)

print("\nResultados:")
print(f"MLP Accuracy: {test_acc_mlp}")
print(f"CNN Accuracy: {test_acc_cnn}")
print(f"RNN Accuracy: {test_acc_rnn}")