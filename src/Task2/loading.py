
"""
  Load raw data from files.
"""

###########################################################################
# Load data.
###########################################################################

def load():

  # Import libraries.
  import pandas as pd
  import numpy as np

  # Disable pandas warnings.
  pd.options.mode.chained_assignment = None

  # Load signature samples.
  for user in range(1, 41):

    # Log user.
    print('Loading user ' + str(user) + '...')

    # Load a user's samples.
    samples = pd.read_csv('./Input/Task2/U1S1.TXT', delimiter=' ', skiprows=1, names=['x', 'y', 'time', 'button', 'azimuth', 'altitude', 'pressure'])

    samples['user'] = pd.Series()
    samples['user'] = 1

    samples['signature'] = pd.Series()
    samples['signature'] = 1

    samples['genuine'] = pd.Series()
    samples['genuine'] = 1

    for sample in range(2, 41):
      data = pd.read_csv('./Input/Task2/U' + str(user) + 'S' + str(sample) + '.TXT', delimiter=' ', skiprows=1, names=['x', 'y', 'time', 'button', 'azimuth', 'altitude', 'pressure'])
      
      data['user'] = pd.Series()
      data['user'] = user

      data['signature'] = pd.Series()
      data['signature'] = sample
      
      data['genuine'] = pd.Series()
      if sample < 21:
        data['genuine'] = 1
      else:
        data['genuine'] = 0

      samples = samples.append(data)

    # Write samples to file.
    samples.to_csv('./Task2/Data/Input/user' + str(user) + '.csv', index=False)

  return samples
