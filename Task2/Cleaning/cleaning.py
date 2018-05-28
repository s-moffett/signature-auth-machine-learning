"""
  Cleans data.
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

# Disable pandas warnings
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
  data = pd.read_csv('/home/seth/Documents/Classes/Biometrics/Project/Workspace/Data/CSV/Task2/user' + user + '.csv', sep=',', skiprows=0)

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
    df = pd.DataFrame([[0, 0, end_time, 0, 0, 0, 0, int(user), i+1, genuine]], columns=['x', 'y', 'time', 'button', 'azimuth', 'altitude', 'pressure', 'user', 'signature', 'genuine'])
    u1_samples[i] = u1_samples[i].append(df)
    end_time += 10

###########################################################################
# Output to file.
###########################################################################

print('Writing clean data to csv...')

for i in range(0, len(u1_samples)):
  if i == 0:
    u1_samples[i].to_csv('./Task2/Cleaning/Data/clean_user' + user + '.csv', mode='w', header=True, index=False)
  else:
    u1_samples[i].to_csv('./Task2/Cleaning/Data/clean_user' + user + '.csv', mode='a', header=False, index=False)
