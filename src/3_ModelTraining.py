# First we need to read in the required packages
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, models

# loading the saved numpy arrays in the previous code
data=np.load('data.npy')
target=np.load('target.npy')

# Split data into training & testing sets
train_data,test_data,train_target,test_target=train_test_split(data,target,test_size=0.1)

"""
In our model we include two convolutional 2D layers, two
max pooling layers, two dropout layers to avoid overfitting, 
a flatten layer, and finally two dense layers to match
the number of classes in the output
"""
model = models.Sequential([
    # The first CNN layer is a Convolution layer of a kernel size 3*3
    # It learns the base features and applies'relu' nonlinear transformation.
    # Also specifying the input shape here to be 100
    layers.Conv2D(100,(3,3), activation='relu', input_shape=data.shape[1:]),
    # MaxPooling2D((2, 2)) 2*2 the size of window to find the max
    layers.MaxPooling2D((2, 2)),
    # layers.Dropout(0.5) force the model to not fit too closely, help relieve overfitting
    layers.Dropout(0.5),
    # The second convolution layer
    layers.Conv2D(100,(3,3), activation='relu'),
    # MaxPooling layer
    layers.MaxPooling2D((2, 2)),
    # Flatten layer to stack the output convolutions from second convolution layer
    layers.Flatten(),
    # layers.Dropout(0.5) force the model to not fit too closely, help relieve overfitting
    layers.Dropout(0.5),
    # Dense layer of 25 neurons
    layers.Dense(25, activation='relu'),
    layers.Dense(2,activation='softmax')
])

# compile the model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
# from_logits=True compute softmax when evaluting loss function
# metrics=['accuracy'] want to see how accurate on the data

# fit the model on 80% of the training set, evaluate on the rest
history = model.fit(train_data,
                     train_target, 
                     epochs=20,
                     validation_split=0.2)

print(model.evaluate(test_data,test_target))