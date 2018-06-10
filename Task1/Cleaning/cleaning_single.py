"""
    Cleans data.
"""

###########################################################################
# Import libraries.
###########################################################################
import pandas as pd
import numpy as np

###########################################################################
# Load data from txt files.
###########################################################################

# List containing each user's list of signatures.
users = []
labels = []

print('Loading data...')

for user in range(1, 41):

    user_signatures = pd.DataFrame(columns=['x', 'y', 'time', 'button'])

    for sig in range(1, 41):
    
        # Get the signature
        signature = pd.read_csv('./Data/CSV/Input/Task1/U' + str(user) + 'S' + str(sig) + '.TXT', sep=' ', skiprows=1, names=['x', 'y', 'time', 'button'])        

        # Add signature field
        signature['signature'] = sig

        # Add the label
        if sig < 21:
            signature['genuine'] = 1
        else:
            signature['genuine'] = 0

        user_signatures = user_signatures.append(signature)
    
    users.append(user_signatures)

















# ###########################################################################
# # Clean data.
# ###########################################################################

# metrics = []

# print('Zeroing data...')
# for user in range(0, len(users)):

#   # User-scoped metrics
#   user_max_records = 0
#   user_max_x = 0
#   user_max_y = 0
#   user_max_time = 0

#   for sig in range(0, len(users[user])):

#     # Time, x, and y should start at 0.
#     #   These values are only meaningful relative to each signature's lowest value,
#     #   so each signature can start at 0.
#     users[user][sig]['time'] = users[user][sig]['time'] - users[user][sig]['time'].min()
#     users[user][sig]['x'] = users[user][sig]['x'] - users[user][sig]['x'].min()
#     users[user][sig]['y'] = users[user][sig]['y'] - users[user][sig]['y'].min()

#     # Check if signature contributes to user's metrics.
#     if users[user][sig]['time'].count() > user_max_records:
#       user_max_records = users[user][sig]['time'].count()
#       # print('Records = ' + str(user_max_records) + ' at user ' + str(user) + ', sig ' + str(sig))

#     if users[user][sig]['x'].max() > user_max_x:
#       user_max_x = users[user][sig]['x'].max()  
#       # print('X = ' + str(user_max_x) + ' at user ' + str(user) + ', sig ' + str(sig))

#     if users[user][sig]['y'].max() > user_max_y:
#       user_max_y = users[user][sig]['y'].max()
#       # print('Y = ' + str(user_max_y) + ' at user ' + str(user) + ', sig ' + str(sig))

#     if users[user][sig]['time'].max() > user_max_time:
#       user_max_time = users[user][sig]['time'].max()
#       # print('Time = ' + str(user_max_time) + ' at user ' + str(user) + ', sig ' + str(sig))

#   # Save the user's metrics.
#   metrics.append([user_max_records, user_max_x, user_max_y, user_max_time])

# ###########################################################################
# # Add records.
# ###########################################################################

# for user in range(0, len(users)):    
#   for sig in range(0, len(users[user])):

#     print('Adding records to user ' + str(user) + ' sig ' + str(sig))

#     # Time, x, and y should be in range 0-1.
#     #   The actual range of values found in a particular signature may be useful compared
#     #   to the other signatures, so values should be scaled relative to the user's
#     #   max values.
#     users[user][sig]['time'] = users[user][sig]['time'] / metrics[user][3]
#     users[user][sig]['x'] = users[user][sig]['x'] / metrics[user][1]
#     users[user][sig]['y'] = users[user][sig]['y'] / metrics[user][2]

#     # All signatures for a given user should be the same length.
#     max_time = users[user][sig]['time'].max() + 10

#     for i in range(0, user_max_records - users[user][sig]['time'].count()):
#       users[user][sig] = users[user][sig].append(pd.DataFrame([[0, 0, max_time, 0]], columns=['x', 'y', 'time', 'button']))
#       max_time += 10
    
#     # Write signature to CSV file.
#     users[user][sig].to_csv('./Task1/Cleaning/Data/clean_u' + str(user + 1) + 's' + str(sig + 1) + '.csv')

