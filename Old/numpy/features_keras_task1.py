###########################################################################
# Import libraries.
###########################################################################
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

pd.options.mode.chained_assignment = None

###########################################################################
# Load data.
#
#   Columns:
#     x, y, time, button, azimuth, altitude, pressure, genuine
#
###########################################################################

print('')
print('Loading data...')

data_source = 0
data = pd.DataFrame()

# Linux
if data_source == 0:
  data = pd.read_csv('/home/seth/Documents/Classes/Biometrics/Project/Data/output/user1.csv', sep=',', skiprows=0)

# Mac
if data_source == 1:
  data = pd.read_csv('/Users/sethmoffett/Documents/Docs/Classes/Biometrics/Project/Dataset2/user1.csv', sep=',', skiprows=0)

###########################################################################
# Separate the signature samples.
###########################################################################

u1_samples = []
for sample_index in range(1, 41):
  u1_samples.append(data.loc[data['signature'] == sample_index])

###########################################################################
# Clean each sample's data.
###########################################################################

print('Cleaning data...')

for sample in u1_samples:

  # The sample time, x, and y are relative and should start at 0.
  sample['time'] = sample['time'] - sample['time'].min()  
  sample['x'] = sample['x'] - sample['x'].min()
  sample['y'] = sample['y'] - sample['y'].min()

  # Sample azimuth, altitude, and pressure should stay as they are
  #   so we can compare to other samples.

###########################################################################
# Find the max number of rows in any sample.
###########################################################################

list_total_samples = []
for sample in u1_samples:
  list_total_samples.append(sample['time'].count())

series_total_samples = pd.Series(list_total_samples)
max_rows = series_total_samples.max()    # 215

###########################################################################
# Add rows to each sample so they're even.
###########################################################################

print('Filling in missing data...')

for i in range(0, len(u1_samples)):
  end_time = u1_samples[i]['time'].max() + 10
  genuine = 0

  if i < 20:
    genuine = 1

  for i2 in range(0, max_rows - u1_samples[i]['time'].count()):
    df = pd.DataFrame([[0, 0, end_time, 0, 0, 0, 0, 0, 0, genuine]], columns=['x', 'y', 'time', 'button', 'azimuth', 'altitude', 'pressure', 'user', 'signature', 'genuine'])
    u1_samples[i] = u1_samples[i].append(df)
    end_time += 10

###########################################################################
# Create total time feature.
###########################################################################

print('')
print('Creating total time feature...')

list_total_time = []

for sample in u1_samples:
  list_total_time.append(sample['time'].max() - sample['time'].min())

np_feature_time = np.array(list_total_time)

###########################################################################
# Create x feature.
###########################################################################

print('Creating x feature...')
list_x = []

for sample in u1_samples:
  list_sample_x = []
  x_start = 0
  x_end = 5

  while x_end < len(sample['x']):
    list_sample_x.append(sample['x'][x_start:x_end].mean())
    x_start += 5
    x_end += 5

  list_x.append(list_sample_x)

np_feature_x = np.array(list_x)
np_feature_x = np_feature_x / np.amax(np_feature_x)

###########################################################################
# Create y feature.
###########################################################################

print('Creating y feature...')
list_y = []

for sample in u1_samples:
  list_sample_y = []
  y_start = 0
  y_end = 5

  while y_end < len(sample['y']):
    list_sample_y.append(sample['y'][y_start:y_end].mean())
    y_start += 5
    y_end += 5

  list_y.append(list_sample_y)

np_feature_y = np.array(list_y)
np_feature_y = np_feature_y / np.amax(np_feature_y)

###########################################################################
# Create genuine label.
###########################################################################

list_genuine = []

for sample in u1_samples:
  list_genuine.append(sample['genuine'].mean())

np_label_genuine = np.array(list_genuine)

###########################################################################
# Merge features into a mega-feature for each samle.
###########################################################################

input_features = [
  # np_feature_time,
  np_feature_x,
  np_feature_y,
  # np_label_genuine
]

samples = []
features = []
labels = []

# For each sample
for i in range(0, 40):

  mega_features = np.array([])

  for j in range(0, 2):
    mega_features = np.concatenate((mega_features, input_features[j][i]), axis=0)

  mega_features = np.append(mega_features, np_feature_time[i])
  
  # Uncomment for 'samples.csv'
  # mega_features = np.append(mega_features, np_label_genuine[i])

  # Add them all in to samples array.
  samples.append(mega_features)

  features.append(mega_features)
  labels.append(np_label_genuine[i])


np.savetxt('samples_task1.csv', samples)
np.savetxt('features_task1.csv', features)
np.savetxt('labels_task1.csv', labels)
