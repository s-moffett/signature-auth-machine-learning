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
    data = pd.read_csv('./Task1/Data/Cleaning/clean_user' + str(user) + '.csv', index_col=False)

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

    # Create 'Genuine' label.
    list_genuine = []

    for sample in samples:
      list_genuine.append(sample['genuine'].mean())

    np_label_genuine = np.array(list_genuine)

    # Merge features into a mega-feature row for each sample.
    input_features = [
      np_feature_x,
      np_feature_y,
    ]             

    features = []
    labels = []

    # For each sample.
    for i in range(0, 40):
      mega_features = np.array([])

      # For each feature.
      for j in range(0, 2):
        mega_features = np.concatenate((mega_features, input_features[j][i]), axis=0)

      features.append(mega_features)
      labels.append(np_label_genuine[i])        

    np.savetxt('./Task1/Data/Features/features_user' + str(user) + '.csv', features)
    np.savetxt('./Task1/Data/Features/labels_user' + str(user) + '.csv', labels)

  return
