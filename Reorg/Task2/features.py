"""
  Creates features.
"""

###########################################################################
# Create features.
###########################################################################
def create_features():

  # Import libraries.
  import pandas as pd
  import numpy as np

  # Disable pandas warnings.
  pd.options.mode.chained_assignment = None

  # Clean each user's features.
  for user in range(1, 41):

    # Log user.
    print('Creating features for user ' + str(user) + '...')

    # Load data.
    print('\tLoading data...')
    data = pd.read_csv('./Task2/Data/Cleaning/clean_user' + str(user) + '.csv', index_col=False)

    # Separate the signature samples.
    samples = []
    for i in range(1, 41):
      samples.append(data.loc[data['signature'] == i])
    
    print('\tCreating features...')

    # Create 'Total Time' feature.
    list_total_time = []
    for sample in samples:
      list_total_time.append(sample['time'].max() - sample['time'].min())
    
    np_feature_time = np.array(list_total_time)

    # Create 'X' feature.
    list_x = []

    for sample in samples:
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

    # Create 'Y' feature.
    list_y = []

    for sample in samples:
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

    # Create 'Azimuth' feature.
    list_azimuth = []

    for sample in samples:
      list_sample_azimuth = []
      azimuth_start = 0
      azimuth_end = 5

      while azimuth_end < len(sample['azimuth']):
        list_sample_azimuth.append(sample['azimuth'][azimuth_start:azimuth_end].mean())
        azimuth_start += 5
        azimuth_end += 5
      list_azimuth.append(list_sample_azimuth)

    np_feature_azimuth = np.array(list_azimuth)
    np_feature_azimuth = np_feature_azimuth / np.amax(np_feature_azimuth)

    # Create 'Altitude' feature.
    list_altitude = []

    for sample in samples:
      list_sample_altitude = []
      altitude_start = 0
      altitude_end = 5

      while altitude_end < len(sample['altitude']):
        list_sample_altitude.append(sample['altitude'][altitude_start:altitude_end].mean())
        altitude_start += 5
        altitude_end += 5
      list_altitude.append(list_sample_altitude)

    np_feature_altitude = np.array(list_altitude)
    np_feature_altitude = np_feature_altitude / np.amax(np_feature_altitude)

    # Create 'Pressure' feature.
    list_pressure = []

    for sample in samples:
      list_sample_pressure = []
      pressure_start = 0
      pressure_end = 5

      while pressure_end < len(sample['pressure']):
        list_sample_pressure.append(sample['pressure'][pressure_start:pressure_end].mean())
        pressure_start += 5
        pressure_end += 5

      list_pressure.append(list_sample_pressure)

    np_feature_pressure = np.array(list_pressure)
    np_feature_pressure = np_feature_pressure / np.amax(np_feature_pressure)

    # Create 'Genuine' label.
    list_genuine = []

    for sample in samples:
      list_genuine.append(sample['genuine'].mean())

    np_label_genuine = np.array(list_genuine)

    # Merge features into a mega-feature row for each sample.
    input_features = [
      np_feature_x,
      np_feature_y,
      np_feature_azimuth,
      np_feature_altitude,
      np_feature_pressure,
    ]

    features = []
    labels = []

    # For each sample.
    for i in range(0, 40):
      mega_features = np.array([])

      # For each feature.
      for j in range(0, 5):
        mega_features = np.concatenate((mega_features, input_features[j][i]), axis=0)

      features.append(mega_features)
      labels.append(np_label_genuine[i])

    np.savetxt('./Task2/Data/Features/features_user' + str(user) + '.csv', features)
    np.savetxt('./Task2/Data/Features/labels_user' + str(user) + '.csv', labels)

  return
