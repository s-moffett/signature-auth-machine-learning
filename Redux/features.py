"""
    Creates features.
"""

###########################################################################
# Import libraries.
###########################################################################
import pandas as pd
import numpy as np

# Disable pandas warnings
pd.options.mode.chained_assignment = None

###########################################################################
# Convert signatures into a single feature row and average every few samples.
###########################################################################
def features_task_1():

  for user in range(1, 41):
    
    # Read all the user's signatures from a CSV.
    raw_signatures = pd.read_csv('./Redux/Data/Cleaning/clean_user' + str(user) + '.csv')

    # Separate the user's signatures.
    signatures = []
    for sig in range(1, 41):
      signatures.append( raw_signatures.loc[raw_signatures['signature'] == sig] )

    # Sample the signature data.
    print('Sampling signatures...')
    
    sampled_signatures_x = []
    sampled_signatures_y = []
    sampled_signatures_time = []

    for sig in range(0, 40):      
      
      # x
      this_signature_sampled_x = []            
      x_start = 0
      x_end = 5

      while x_end < len(signatures[sig]['x']):
        this_signature_sampled_x.append( signatures[sig]['x'][x_start:x_end].mean() )
        x_start += 5
        x_end += 5

      this_signature_sampled_x.append( signatures[sig]['x'][x_end:len(signatures[sig]['x'])].mean() )      
      sampled_signatures_x.append(this_signature_sampled_x)

      # y
      this_signature_sampled_y = []
      y_start = 0
      y_end = 5

      while y_end < len(signatures[sig]['y']):
        this_signature_sampled_y.append( signatures[sig]['y'][y_start:y_end].mean() )
        y_start += 5
        y_end += 5
      
      this_signature_sampled_y.append( signatures[sig]['y'][y_end:len(signatures[sig]['y'])].mean() )
      sampled_signatures_y.append(this_signature_sampled_y)

      # time
      this_signature_sampled_time = []
      time_start = 0
      time_end = 5

      while time_end < len(signatures[sig]['time']):
        this_signature_sampled_time.append( signatures[sig]['time'][time_start:time_end].mean() )
        time_start += 5
        time_end += 5
      
      this_signature_sampled_time.append( signatures[sig]['time'][time_end:len(signatures[sig]['time'])].mean() )
      sampled_signatures_time.append(this_signature_sampled_time)
    

    # Merge each signature's data into a single feature row (one for each signature).
    features = []
    labels = []
    
    for sig in range(0, 40):      
      feature_row = np.array([])
      feature_row = np.concatenate((feature_row, np.array(sampled_signatures_x[sig])), axis=0)
      feature_row = np.concatenate((feature_row, np.array(sampled_signatures_y[sig])), axis=0)
      feature_row = np.concatenate((feature_row, np.array(sampled_signatures_time[sig])), axis=0)
      features.append(feature_row)

      if sig < 21:
        labels.append(1)
      else:
        labels.append(0)

    # Write each user's data to CSV.
    np.savetxt('./Redux/Data/Features/features_user' + str(user) + '.csv', features, delimiter=',')
    np.savetxt('./Redux/Data/Features/labels_user' + str(user) + '.csv', labels, delimiter=',')

  return


###########################################################################
# For testing.
###########################################################################
  
if __name__ == '__main__':
  features_task_1()
