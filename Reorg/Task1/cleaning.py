"""
  Cleaning methods.
"""

###########################################################################
# Clean signature samples.
###########################################################################
def clean():

  # Import libraries.
  import pandas as pd
  import numpy as np

  # Disable pandas warnings.
  pd.options.mode.chained_assignment = None

  # Clean each user's samples.
  for user in range(1, 41):

    # Log user.
    print('Cleaning user ' + str(user) + '...')

    # Load data.
    print('\tLoading data...')
    data = pd.read_csv('./Task2/Data/Input/user' + str(user) + '.csv')

    # Separate the samples.
    samples = []
    for i in range(1, 41):
      samples.append(data.loc[data['signature'] == i])

    # Zero x, y, and time.
    print('\tCleaning data...')
    for sample in samples:
      sample['time'] = sample['time'] - sample['time'].min()  
      sample['x'] = sample['x'] - sample['x'].min()
      sample['y'] = sample['y'] - sample['y'].min()

    # Find the max number of rows in any sample.
    sample_totals = []

    for sample in samples:
      sample_totals.append(sample['time'].count())

    series_sample_totals = pd.Series(sample_totals)
    max_rows = series_sample_totals.max()
  
    # Add rows to each sample so they're even.
    print('\tAdding rows...')
    for i in range(0, len(samples)):
      
      # Get last time value.
      end_time = samples[i]['time'].max() + 10
      
      # Set genuine label.
      genuine = 0
      if i < 20:
        genuine = 1

      # Insert rows.
      for j in range(0, max_rows - samples[i]['time'].count()):
        df = pd.DataFrame([[0, 0, end_time, user, i+1, genuine]], columns=['x', 'y', 'time', 'user', 'signature', 'genuine'])
        samples[i] = samples[i].append(df)
        end_time += 10

    # Output cleaned sample to file.
    print('\tWriting data to file...')
    for i in range(0, len(samples)):
      if i == 0:
        samples[i].to_csv('./Task1/Data/Cleaning/clean_user' + user + '.csv', mode='w', header=True, index=False)
      else:
        samples[i].to_csv('./Task1/Data/Cleaning/clean_user' + user + '.csv', mode='a', header=False, index=False)
  
  return
