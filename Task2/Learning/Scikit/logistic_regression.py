
###########################################################################
# Configuration.
###########################################################################

user = '1'

###########################################################################
# Import libraries.
###########################################################################
import numpy as np
from matplotlib import pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

###########################################################################
# Load features.
###########################################################################

features = np.loadtxt('./Task2/Features/Data/Sampled/features_user' + user + '.csv')
labels = np.loadtxt('./Task2/Features/Data/Sampled/labels_user' + user + '.csv')

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.25)

###########################################################################
# Create logistic regression model and train.
###########################################################################

classifier = LogisticRegression(penalty='l1', solver='liblinear')
classifier.fit(features_train, labels_train)

###########################################################################
# Score results.
###########################################################################

# Metrics
sparsity = np.mean(classifier.coef_ == 0) * 100
score = classifier.score(features_test, labels_test)
print('Score: ' + str(score))

# Test results
test_predictions = classifier.predict(features_test[0:10])
for i in range(0, len(test_predictions)):  
  print('Test - Predicted: ' + str(test_predictions[i]) + ' Actual: ' + str(labels_test[i]))

