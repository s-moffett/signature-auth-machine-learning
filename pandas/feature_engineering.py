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

data_source = 1
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

feature_total_time = pd.Series(list_total_time)

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

feature_x = pd.Series(list_x)

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

feature_y = pd.Series(list_y)

###########################################################################
# Create azimuth feature.
###########################################################################

print('Creating azimuth feature...')
list_azimuth = []

for sample in u1_samples:
  list_sample_azimuth = []
  azimuth_start = 0
  azimuth_end = 5

  while azimuth_end < len(sample['azimuth']):
    list_sample_azimuth.append(sample['azimuth'][azimuth_start:azimuth_end].mean())
    azimuth_start += 5
    azimuth_end += 5

  list_azimuth.append(list_sample_azimuth)

feature_azimuth = pd.Series(list_azimuth)

###########################################################################
# Create altitude feature.
###########################################################################

print('Creating altitude feature...')
list_altitude = []

for sample in u1_samples:
  list_sample_altitude = []
  altitude_start = 0
  altitude_end = 5

  while altitude_end < len(sample['altitude']):
    list_sample_altitude.append(sample['altitude'][altitude_start:altitude_end].mean())
    altitude_start += 5
    altitude_end += 5

  list_altitude.append(list_sample_altitude)

feature_altitude = pd.Series(list_altitude)

###########################################################################
# Create pressure feature.
###########################################################################

print('Creating pressure feature...')
list_pressure = []

for sample in u1_samples:
  list_sample_pressure = []
  pressure_start = 0
  pressure_end = 5

  while pressure_end < len(sample['pressure']):
    list_sample_pressure.append(sample['pressure'][pressure_start:pressure_end].mean())
    pressure_start += 5
    pressure_end += 5

  list_pressure.append(list_sample_pressure)

feature_pressure = pd.Series(list_pressure)

###########################################################################
# Create genuine label.
###########################################################################

list_genuine = []

for sample in u1_samples:
  list_genuine.append(sample['genuine'].mean())

label_genuine = pd.Series(list_genuine)

###########################################################################
# Features:
#   Total time
#   Samples of x, y, azimuth, altitude, pressure  
#
# Label:
#   genuine
###########################################################################

###########################################################################
# Scale total time feature.
###########################################################################

print('')
print('Scaling total time feature...')

# Zero feature_total_time.
feature_total_time = feature_total_time - feature_total_time.min()

# Get max time in feature_total_time.
max_time = feature_total_time.max()

# Scale feature_total_time.
feature_total_time = feature_total_time / max_time

###########################################################################
# Scale x feature.
###########################################################################

print('Scaling x feature...')
list_max_x = []

# Get max x in feature_x.
for i in range(0, feature_x.count()):
  list_max_x.append(pd.Series(feature_x[i]).max())

series_max_x = pd.Series(list_max_x)
max_x = series_max_x.max()

# Scale feature_x.
for i in range(0, feature_x.count()):
  feature_x[i] = feature_x[i] / max_x

###########################################################################
# Scale y feature.
###########################################################################

print('Scaling y feature...')
list_max_y = []

# Get max y in feature_y.
for i in range(0, feature_y.count()):
  list_max_y.append(pd.Series(feature_y[i]).max())

series_max_y = pd.Series(list_max_y)
max_y = series_max_y.max()

# Scale feature_y.
for i in range(0, feature_y.count()):
  feature_y[i] = feature_y[i] / max_y

###########################################################################
# Scale azimuth feature.
###########################################################################

print('Scaling azimuth feature...')
list_max_azimuth = []

# Get max azimuth in feature_azimuth.
for i in range(0, feature_azimuth.count()):
  list_max_azimuth.append(pd.Series(feature_azimuth[i]).max())

series_max_azimuth = pd.Series(list_max_azimuth)
max_azimuth = series_max_azimuth.max()

# Scale feature_azimuth
for i in range(0, feature_azimuth.count()):
  feature_azimuth[i] = feature_azimuth[i] / max_azimuth

###########################################################################
# Scale altitude feature.
###########################################################################

print('Scaling altitude feature...')
list_max_altitude = []

# Get max altitude in feature_altitude.
for i in range(0, feature_altitude.count()):
  list_max_altitude.append(pd.Series(feature_altitude[i]).max())

series_max_altitude = pd.Series(list_max_altitude)
max_altitude = series_max_altitude.max()

# Scale feature_altitude
for i in range(0, feature_altitude.count()):
  feature_altitude[i] = feature_altitude[i] / max_altitude

###########################################################################
# Scale pressure feature.
###########################################################################

print('Scaling pressure feature...')
list_max_pressure = []

# Get max pressure in feature_pressure
for i in range(0, feature_pressure.count()):
  list_max_pressure.append(pd.Series(feature_pressure[i]).max())

series_max_pressure = pd.Series(list_max_pressure)
max_pressure = series_max_pressure.max()

# Scale feature_pressure
for i in range(0, feature_pressure.count()):
  feature_pressure[i] = feature_pressure[i] / max_pressure

###########################################################################
# Save features to pkl files.
###########################################################################

# .pkl files
d = {'total_time': feature_total_time, 'x': feature_x, 'y': feature_y, 'azimuth': feature_azimuth, 'altitude': feature_altitude, 'pressure': feature_pressure}
features = pd.DataFrame(d)
# features.to_pickle('features.pkl')

d2 = {'genuine': label_genuine}
labels = pd.DataFrame(d2)
# labels.to_pickle('labels.pkl')

###########################################################################
# Save separated data to csv file.
###########################################################################

# Split data into training and test sets.
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.25)
all_train = pd.concat([features_train, labels_train], axis=1)
all_test = pd.concat([features_test, labels_test], axis=1)

# csv files
all_train.to_csv('train.csv')
all_test.to_csv('test.csv')

