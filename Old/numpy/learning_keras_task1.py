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

samples = np.loadtxt('samples_task1.csv')
features = np.loadtxt('features_task1.csv')
labels = np.loadtxt('labels_task1.csv')

###########################################################################
# Separate training and test sets.
###########################################################################

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.25)

labels_train_binary = to_categorical(labels_train)
labels_test_binary = to_categorical(labels_test)

###########################################################################
# Create neural network.
###########################################################################

model = Sequential()
model.add(Dense(units=64, activation='sigmoid', input_dim=85))
model.add(Dense(units=100, activation='sigmoid'))
model.add(Dense(units=64, activation='sigmoid'))
model.add(Dense(units=10, activation='sigmoid'))
model.add(Dense(units=1, activation='sigmoid'))

opt = SGD(lr=0.00001)

model.compile(loss='mean_squared_error',
              optimizer='rmsprop',
              metrics=['accuracy'])

###########################################################################
# Train model.
###########################################################################

# Mean squared error
model.fit(features_train, labels_train, epochs=1000, batch_size=30)
loss_and_metrics = model.evaluate(features_test, labels_test, batch_size=10)
print(loss_and_metrics)
