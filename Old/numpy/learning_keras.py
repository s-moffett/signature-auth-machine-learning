###########################################################################
# Import libraries.
###########################################################################
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers import Activation, Dense
from keras.utils import to_categorical
from keras.optimizers import SGD

###########################################################################
# Load data from csv files.
###########################################################################

samples = np.loadtxt('samples.csv')
features = np.loadtxt('features.csv')
labels = np.loadtxt('labels.csv')

###########################################################################
# Separate training and test sets.
###########################################################################

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.25)

labels_train_binary = to_categorical(labels_train)
labels_test_binary = to_categorical(labels_test)

###########################################################################
# Create neural network.
###########################################################################

# user1   input_dim=211
# user2   input_dim=236

# user4   input_dim=241

model = Sequential()
model.add(Dense(units=64, activation='sigmoid', input_dim=171))
model.add(Dense(units=100, activation='sigmoid'))
model.add(Dense(units=64, activation='sigmoid'))
model.add(Dense(units=10, activation='sigmoid'))
model.add(Dense(units=2, activation='sigmoid'))

opt = SGD(lr=0.0001)

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

###########################################################################
# Train model.
###########################################################################

# Mean squared error
model.fit(features_train, labels_train_binary, epochs=1000, batch_size=30)
loss_and_metrics = model.evaluate(features_test, labels_test_binary, batch_size=10)

with open('results.txt', 'a') as f:
  f.write('User 3\n')
  f.write(str(loss_and_metrics) + '\n')
  f.write('\n')

