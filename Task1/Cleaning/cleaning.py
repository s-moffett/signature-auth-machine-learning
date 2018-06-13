"""
  Cleans data.
"""

###########################################################################
# Import libraries.
###########################################################################
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

# Disable pandas warnings
pd.options.mode.chained_assignment = None

for user in range(1, 41):

  print('')
  print('User ' + str(user) + ':')
  print('Loading data...')

  # Load data.
  data = pd.read_csv('./Redux/Data/Loading/user' + str(user) + '.csv', sep=',', skiprows=0)
  data['user'] = user

  # Separate the signatures.
  signatures = []
  for sig in range(1, 41):
    signatures.append(data.loc[data['signature'] == sig])

  print('Cleaning data...')

  # Clean each signature.
  # The signature time, x, and y are relative and should start at 0.
  for signature in signatures:
    signature['time'] = signature['time'] - signature['time'].min()  
    signature['x'] = signature['x'] - signature['x'].min()
    signature['y'] = signature['y'] - signature['y'].min()

  # Get max number of rows in any signature.
  list_total_rows = []
  for signature in signatures:
    list_total_rows.append(signature['time'].count())

  series_total_rows = pd.Series(list_total_rows)
  max_rows = series_total_rows.max()

  print('Filling in missing data...')

  # Add rows to each sample so they're even.
  for i in range(0, len(signatures)):
    
    print('\t signature ' +str(i))
    end_time = signatures[i]['time'].max() + 10
    genuine = 0

    if i < 20:
      genuine = 1

    for i2 in range(0, max_rows - signatures[i]['time'].count()):
      df = pd.DataFrame([[0, 0, end_time, 0, user, i+1, genuine]], columns=['x', 'y', 'time', 'button', 'user', 'signature', 'genuine'])
      signatures[i] = signatures[i].append(df)
      end_time += 10

  # Output to file.
  print('Writing clean data to csv...')

  for i in range(0, len(signatures)):
    if i == 0:
      signatures[i].to_csv('./Task1/Cleaning/Data/clean_user' + str(user) + '.csv', mode='w', header=True, index=False)
    else:
      signatures[i].to_csv('./Task1/Cleaning/Data/clean_user' + str(user) + '.csv', mode='a', header=False, index=False)
