
###########################################################################
# Import libraries.
###########################################################################
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

###########################################################################
# Read data.
###########################################################################

data = pd.read_csv('./Task2/Learning/Keras/ROC/roc_user1.csv')

for i in range(2, 41):
  new_data = pd.read_csv('./Task2/Learning/Keras/ROC/roc_user' + str(i) + '.csv')
  data = data.append(new_data)

###########################################################################
# Calculate FAR and FRR for 0.5 threshold.
###########################################################################

threshold = 0.5

false_positives = data.loc[np.logical_and(data['Prediction'] < threshold, data['Label'] == 1)]
false_negatives = data.loc[np.logical_and(data['Prediction'] >= threshold, data['Label'] == 0)]

true_positives = data.loc[np.logical_and(data['Prediction'] > threshold, data['Label'] == 1)]
true_negatives = data.loc[np.logical_and(data['Prediction'] < threshold, data['Label'] == 0)]

FAR = false_positives.count() / (false_positives.count() + true_negatives.count())
FRR = 1 - (true_positives.count() / (true_positives.count() + false_negatives.count()))

FAR = FAR['Label']
FRR = FRR['Label']

print('Threshold = 0.5')
print('FAR: ' + str(FAR))
print('FRR: ' + str(FRR))

###########################################################################
# Create ROC curve.
###########################################################################

ROC = pd.DataFrame([[0, 0, 1]], columns=['Threshold', 'FAR', 'FRR'])

for int_threshold in range(1, 100):

  threshold = int_threshold / 100

  false_positives = data.loc[np.logical_and(data['Prediction'] < threshold, data['Label'] == 1)]
  false_negatives = data.loc[np.logical_and(data['Prediction'] >= threshold, data['Label'] == 0)]

  true_positives = data.loc[np.logical_and(data['Prediction'] > threshold, data['Label'] == 1)]
  true_negatives = data.loc[np.logical_and(data['Prediction'] < threshold, data['Label'] == 0)]

  FAR = false_positives.count() / (false_positives.count() + true_negatives.count())
  FRR = 1 - (true_positives.count() / (true_positives.count() + false_negatives.count()))

  FAR = FAR['Label']
  FRR = FRR['Label']

  ROC = ROC.append( pd.DataFrame([[threshold, FAR, FRR]], columns=['Threshold', 'FAR', 'FRR']) )

ROC = ROC.append( pd.DataFrame([[1, 1, 0]], columns=['Threshold', 'FAR', 'FRR']) )

###########################################################################
# Create simplified ROC data.
###########################################################################

ROC_simplified = pd.DataFrame([[0, 0, 1]], columns=['Threshold', 'FAR', 'FRR'])

for int_threshold in range(1, 10):

  threshold = int_threshold / 10

  false_positives = data.loc[np.logical_and(data['Prediction'] < threshold, data['Label'] == 1)]
  false_negatives = data.loc[np.logical_and(data['Prediction'] >= threshold, data['Label'] == 0)]

  true_positives = data.loc[np.logical_and(data['Prediction'] > threshold, data['Label'] == 1)]
  true_negatives = data.loc[np.logical_and(data['Prediction'] < threshold, data['Label'] == 0)]

  FAR = false_positives.count() / (false_positives.count() + true_negatives.count())
  FRR = 1 - (true_positives.count() / (true_positives.count() + false_negatives.count()))

  FAR = FAR['Label']
  FRR = FRR['Label']

  ROC_simplified = ROC_simplified.append( pd.DataFrame([[threshold, FAR, FRR]], columns=['Threshold', 'FAR', 'FRR']) )

###########################################################################
# Plot ROC curve.
###########################################################################

ROC.to_csv('./Task2/Learning/roc.csv')
ROC_simplified.to_csv('./Task2/Learning/roc_simplified.csv')

plt.plot(ROC['FAR'], ROC['FRR'])
plt.xlabel('FAR')
plt.ylabel('FRR')
plt.show()

