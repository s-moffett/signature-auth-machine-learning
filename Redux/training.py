"""
    Trains the models.
"""

###########################################################################
# Train a neural network.
###########################################################################
def train_task_1_neural_net():

  # Import libraries.
  import pandas as pd
  import numpy as np
  from sklearn.model_selection import train_test_split

  from keras.models import Sequential
  from keras.layers import Dense

  for user in range(1, 41):

    # Load the user's data.
    features = np.loadtxt('./Redux/Data/Features/features_user' + str(user) + '.csv', delimiter=',')
    labels = np.loadtxt('./Redux/Data/Features/labels_user' + str(user) + '.csv', delimiter=',')

    # Separate the data into training and test sets.
    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.25)

    # Create a neural network.
    model = Sequential()
    model.add(Dense(units=64, activation='relu', input_dim=len(features_train[0])))
    model.add(Dense(units=64, activation='relu'))
    model.add(Dense(units=1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy',
                    optimizer='rmsprop',
                    metrics=['binary_accuracy'])

    # Train model.
    model.fit(features_train, labels_train, epochs=100, batch_size=30)

    # Evaluate model.
    loss_and_metrics = model.evaluate(features_test, labels_test, batch_size=10)
    print(loss_and_metrics)

  return


###########################################################################
# For testing.
###########################################################################

if __name__ == '__main__':
  train_task_1_neural_net()
