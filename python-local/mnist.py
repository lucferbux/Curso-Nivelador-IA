import tensorflow as tf
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist

# Load and prepare the MNIST dataset. Convert the samples from integers to floating-point numbers:
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Create the model by stacking layers. Choose an optimizer and loss function for training:
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# For each example the model returns a vector of "logits" or "log-odds" scores, one for each class.
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

# The Model.fit method adjusts the model parameters to minimize the loss
history = model.fit(x_train, y_train, epochs=5)

# Plot the loss curve
plt.xlabel('Epoch Number')
plt.ylabel("Loss Magnitude")
plt.plot(history.history['loss'])
plt.show()

# The Model.evaluate method checks the models performance, usually on a "Validation-set" or "Test-set".
model.evaluate(x_test,  y_test, verbose=2)