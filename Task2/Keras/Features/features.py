
"""
  Creates features.
"""

###########################################################################
# Configuration.
###########################################################################

# Environment
#     Linux = 0
#     Mac = 1
data_source = 0

# User
user = '1'

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
print('Loading clean data...')

data_source = 0
data = pd.DataFrame()

# Linux
if data_source == 0:
  data = pd.read_csv('/home/seth/Documents/Classes/Biometrics/Project/Workspace/Task2/Cleaning/Data/clean_user' + user + '.csv', sep=',', skiprows=0)

# Mac
if data_source == 1:
  data = pd.read_csv('/Users/sethmoffett/Documents/Docs/Classes/Biometrics/Project/Dataset2/user1.csv', sep=',', skiprows=0)

###########################################################################
# Separate the signature samples.
###########################################################################

u1_samples = []
for sample_index in range(1, 41):
  u1_samples.append(data.loc[data['signature'] == sample_index])

# ###########################################################################
# # Create total time feature.
# ###########################################################################

# print('')
# print('Creating total time feature...')

# list_total_time = []

# for sample in u1_samples:
#   list_total_time.append(sample['time'].max() - sample['time'].min())

# np_feature_time = np.array(list_total_time)

# ###########################################################################
# # Create x feature.
# ###########################################################################

# print('Creating x feature...')
# list_x = []

# for sample in u1_samples:
#   list_sample_x = []
#   x_start = 0
#   x_end = 5

#   while x_end < len(sample['x']):
#     list_sample_x.append(sample['x'][x_start:x_end].mean())
#     x_start += 5
#     x_end += 5

#   list_x.append(list_sample_x)

# np_feature_x = np.array(list_x)
# np_feature_x = np_feature_x / np.amax(np_feature_x)

# ###########################################################################
# # Create y feature.
# ###########################################################################

# print('Creating y feature...')
# list_y = []

# for sample in u1_samples:
#   list_sample_y = []
#   y_start = 0
#   y_end = 5

#   while y_end < len(sample['y']):
#     list_sample_y.append(sample['y'][y_start:y_end].mean())
#     y_start += 5
#     y_end += 5

#   list_y.append(list_sample_y)

# np_feature_y = np.array(list_y)
# np_feature_y = np_feature_y / np.amax(np_feature_y)

# ###########################################################################
# # Create azimuth feature.
# ###########################################################################

# print('Creating azimuth feature...')
# list_azimuth = []

# for sample in u1_samples:
#   list_sample_azimuth = []
#   azimuth_start = 0
#   azimuth_end = 5

#   while azimuth_end < len(sample['azimuth']):
#     list_sample_azimuth.append(sample['azimuth'][azimuth_start:azimuth_end].mean())
#     azimuth_start += 5
#     azimuth_end += 5

#   list_azimuth.append(list_sample_azimuth)

# np_feature_azimuth = np.array(list_azimuth)
# np_feature_azimuth = np_feature_azimuth / np.amax(np_feature_azimuth)

# ###########################################################################
# # Create altitude feature.
# ###########################################################################

# print('Creating altitude feature...')
# list_altitude = []

# for sample in u1_samples:
#   list_sample_altitude = []
#   altitude_start = 0
#   altitude_end = 5

#   while altitude_end < len(sample['altitude']):
#     list_sample_altitude.append(sample['altitude'][altitude_start:altitude_end].mean())
#     altitude_start += 5
#     altitude_end += 5

#   list_altitude.append(list_sample_altitude)

# np_feature_altitude = np.array(list_altitude)
# np_feature_altitude = np_feature_altitude / np.amax(np_feature_altitude)

# ###########################################################################
# # Create pressure feature.
# ###########################################################################

# print('Creating pressure feature...')
# list_pressure = []

# for sample in u1_samples:
#   list_sample_pressure = []
#   pressure_start = 0
#   pressure_end = 5

#   while pressure_end < len(sample['pressure']):
#     list_sample_pressure.append(sample['pressure'][pressure_start:pressure_end].mean())
#     pressure_start += 5
#     pressure_end += 5

#   list_pressure.append(list_sample_pressure)

# np_feature_pressure = np.array(list_pressure)
# np_feature_pressure = np_feature_pressure / np.amax(np_feature_pressure)

# ###########################################################################
# # Create genuine label.
# ###########################################################################

# list_genuine = []

# for sample in u1_samples:
#   list_genuine.append(sample['genuine'].mean())

# np_label_genuine = np.array(list_genuine)

# ###########################################################################
# # Merge features into a mega-feature for each samle.
# ###########################################################################

# input_features = [
#   # np_feature_time,
#   np_feature_x,
#   np_feature_y,
#   np_feature_azimuth,
#   np_feature_altitude,
#   np_feature_pressure,
#   # np_label_genuine
# ]

# samples = []
# features = []
# labels = []

# # For each sample
# for i in range(0, 40):

#   mega_features = np.array([])

#   for j in range(0, 5):
#     mega_features = np.concatenate((mega_features, input_features[j][i]), axis=0)

#   mega_features = np.append(mega_features, np_feature_time[i])
  
#   # Uncomment for 'samples.csv'
#   # mega_features = np.append(mega_features, np_label_genuine[i])

#   # Add them all in to samples array.
#   samples.append(mega_features)

#   features.append(mega_features)
#   labels.append(np_label_genuine[i])

# print('User has ' + str(len(samples[0])) + ' features.')

# np.savetxt('samples.csv', samples)
# np.savetxt('features.csv', features)
# np.savetxt('labels.csv', labels)
