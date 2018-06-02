###########################################################################
# Import libraries.
###########################################################################
import numpy as np
import pandas as pd

from matplotlib import pyplot as plt

###########################################################################
# Open logistric regression results.
###########################################################################

lr_results = []

with open('./Task2/Learning/Scikit/Results/results.txt', 'r') as f:
  lr_raw = f.readlines()

for line in lr_raw:
  lr_results.append( float(line.split(':')[1].strip('\n').strip(' ')) )

lr_results = np.array(lr_results[:-1])

plt.plot(lr_results)

###########################################################################
# Open neural network results.
###########################################################################

nn_results = []

with open('./Task2/Learning/Keras/Results/results.txt', 'r') as f:
  nn_raw = f.readlines()

for line in nn_raw:
  nn_results.append( float(line.split(':')[1].strip('\n').strip(' ')) )

nn_results = np.array(nn_results[:-1])

plt.plot(nn_results)

plt.ylabel('Proportion of user\'s test set correctly classified')
plt.xlabel('User ID')
plt.legend(['Logistic regression', 'Neural network'])

plt.show()
