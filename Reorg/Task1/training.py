"""
  Trains the machine learning models.
"""

###########################################################################
# Train the neural network.
###########################################################################
def train_neural_network():

  # Import libraries.
  import pandas as pd
  import numpy as np
  from sklearn.model_selection import train_test_split
  from keras.models import Sequential, Dense

  # Disable pandas warnings.
  pd.options.mode.chained_assignment = None

  # Overwrite any existing results file.
  with open('./Task1/Data/Results/neural_network_results.txt', 'w') as f:
    f.write('')

  # Create a list to store each user's average accuracy.
  total_scores = []    

  for user in range(1, 41):

    # Log user.
    print('Training neural network for user ' + user + '...')

    # Load features.
    features = np.loadtxt('./Task1/Data/Features/features_user' + user + '.csv')
    labels = np.loadtxt('./Task1/Data/Features/labels_user' + user + '.csv')

    # Separate user's samples into training and test datasets.
    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.25)
    num_features = len(features_train[0])

    # Create model.
    model = Sequential()
    model.add(Dense(units=64, activation='relu', input_dim=num_features))
    model.add(Dense(units=64, activation='relu'))
    model.add(Dense(units=1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy',
                    optimizer='rmsprop',
                    metrics=['binary_accuracy'])

    # Train model.
    model.fit(features_train, labels_train, epochs=100, batch_size=30)

    # Evaluate total loss and accuracy for the user's test set.
    loss_and_metrics = model.evaluate(features_test, labels_test, batch_size=10)

    # Calculate our own accuracy based on the probability.
    user_scores = []
    for i in range(0, len(features_test)):
      if labels_test[i] == round(model.predict(features_test[i:i+1], batch_size=1)[0][0]):
        user_scores.append(1)
      else:
        user_scores.append(0)
    
    # Add user's average accuracy to total scores list.
    total_scores.append(user_scores.mean())

    # Write user's average accuracy to file.
    with open('./Task1/Data/Results/neural_network_results.txt', 'a') as f:
      f.write('User ' + user + ': ' + str(user_scores.mean()) + '\n')

  # Write average of all user's accuracies to file.
  total_scores = np.array(total_scores)
  with open('./Task1/Data/Results/neural_network_results.txt', 'a') as f:
    f.write('Total: ' + str(total_scores.mean()) + '\n')

  return

###########################################################################
# Train the logistic regression model.
###########################################################################
def train_logistic_regression():

  # Import libraries.
  import pandas as pd
  import numpy as np
  from sklearn.model_selection import train_test_split
  from sklearn.linear_model import LogisticRegression

  # Disable pandas warnings.
  pd.options.mode.chained_assignment = None

  # Overwrite any existing results file.
  with open('./Task1/Data/Results/logistic_regression_results.txt', 'w') as f:
    f.write('')

  # Create a list to store each user's average accuracy.
  total_scores = []

  for user in range(1, 41):

    # Log user.
    print('Training logistic regression model for user ' + user + '...')

    # Load features.
    features = np.loadtxt('./Task1/Data/Features/features_user' + user + '.csv')
    labels = np.loadtxt('./Task1/Data/Features/labels_user' + user + '.csv')

    # Separate user's samples into training and test datasets.
    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.25)

    # Create model.
    classifier = LogisticRegression(penalty='l1', solver='liblinear')
    
    # Train model.
    classifier.fit(features_train, labels_train)

    # Calculate user's average accuracy.
    score = classifier.score(features_test, labels_test)
    total_scores.append(score)

    # Write user's average accuracy to file.
    with open('./Task1/Data/Results/logistic_regression_results.txt', 'a') as f:
      f.write('')

  # Write average of all user's accuracies to file.
  total_scores = np.array(total_scores)
  with open('./Task1/Data/Results/logistic_regression_results.txt', 'a') as f:
    f.write('Total average accuracy: ' + str(total_scores.mean()) + '\n')

  return
