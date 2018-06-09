###########################################################################
# Import libraries.
###########################################################################
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import plot_model

###########################################################################
# Configuration.
###########################################################################

with open('./Task1/Learning/Keras/Results/results.txt', 'w') as f:
    f.write('')

total_scores = []

for jkl in range(1, 41):

    user = str(jkl)

    ###########################################################################
    # Load features.
    ###########################################################################

    features = np.loadtxt('./Task2/Features/Data/Sampled/features_user' + user + '.csv')
    labels = np.loadtxt('./Task2/Features/Data/Sampled/labels_user' + user + '.csv')

    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.25)
    num_features = len(features_train[0])

    ###########################################################################
    # Create model.
    ###########################################################################

    model = Sequential()
    model.add(Dense(units=64, activation='relu', input_dim=num_features))
    model.add(Dense(units=1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy',
                    optimizer='rmsprop',
                    metrics=['binary_accuracy'])

    ###########################################################################
    # Train model.
    ###########################################################################

    model.fit(features_train, labels_train, epochs=5, batch_size=30)

    ###########################################################################
    # Evaluate.
    ###########################################################################

    user_scores = []

    loss_and_metrics = model.evaluate(features_test, labels_test, batch_size=10)
    print(loss_and_metrics)

    # Training data
    for i in range(0, len(features_train)):
        if labels_train[i] == round(model.predict(features_train[i:i+1], batch_size=1)[0][0]):
            user_scores.append(1)
        else:
            user_scores.append(0)

    training_scores = np.array(user_scores)

    # Test data
    for i in range(0, len(features_test)):    
        if labels_test[i] == round(model.predict(features_test[i:i+1], batch_size=1)[0][0]):
            user_scores.append(1)
        else:
            user_scores.append(0)

    test_scores = np.array(user_scores[len(features_train):len(features_train)+len(features_test)])
    user_scores = np.array(user_scores)
    total_scores.append(test_scores.mean())

    with open('./Task1/Learning/Keras/Results/results.txt', 'a') as f:
        f.write('User ' + user + ': ' + str(test_scores.mean()) + '\n')

total_scores = np.array(total_scores)

with open('./Task1/Learning/Keras/Results/results.txt', 'a') as f:
    f.write('Total: ' + str(total_scores.mean()) + '\n')
