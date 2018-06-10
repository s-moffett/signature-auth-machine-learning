###########################################################################
# Import libraries.
###########################################################################
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers import Dense

###########################################################################
# Load data.
###########################################################################

users = []
labels = []

for user in range(1, 41):

    ###########################################################################
    # Load data.
    ###########################################################################

    user_signatures = []
    user_labels = []
    
    for sig in range(1, 41):
        signature = pd.read_csv('./Task1/Cleaning/Data/clean_u' + str(user) + 's' + str(sig) + '.csv')
        user_signatures.append(signature[['x', 'y', 'time', 'button']].values.tolist())

        if user < 21:
            user_labels.append(1)
        else:
            user_labels.append(0)

    users.append(user_signatures)
    labels.append(user_labels)

###########################################################################
# Split into test and training data.
###########################################################################

users_train = []
users_test = []

labels_train = []
labels_test = []

for user in range(0, 40):
    user_train, user_test, user_labels_train, user_labels_test = train_test_split(users[user], labels[user], test_size=0.25)

    users_train.append(user_train)
    users_test.append(user_test)
    
    labels_train.append(user_labels_train)
    labels_test.append(user_labels_test)



    
np_users = np.asarray(users)
np_labels = np.asarray(labels)

# np_users is now a 40x40 numpy array of signatures, each of which is a 527x4 array


###########################################################################
# Convert data into format for neural network.
###########################################################################

# for user in range(0, 40):
    
#     signature_length = len(np_users[user][0])
    
#     for sig in range(0, 40):
#         np_users[user][sig] = np_users[user][sig].ravel().reshape((527, 4)) 





# list_users = []
# list_labels = labels

# for user in range(0, 40):
    
#     list_user_signatures = []
#     for sig in range(0, 40):


# # Convert list of lists of datasets into numpy arrays
# np_users = []
# np_labels = labels

# for user in range(0, 40):
#     np_user_signatures = []
#     for sig in range(0, 40):
#         np_user_signatures.append(users[user][sig].values.tolist())

#     np_users.append(np_user_signatures)

# # np_users = np.array(np_users)
# # np_labels = np.array(labels)

# ###########################################################################
# # Split data into training and test.
# ###########################################################################

users_train = []
users_test = []

labels_train = []
labels_test = []

for user in range(0, 40):
    user_train, user_test, user_labels_train, user_labels_test = train_test_split(users[user], labels[user], test_size=0.25)

    users_train.append(user_train)
    users_test.append(user_test)
    
    labels_train.append(user_labels_train)
    labels_test.append(user_labels_test)

# for user in range(0, 40):
#     for sig in range(0, 30):
#         users_train[user][sig] = np.array(users_train[user][sig])

# users_train = np.array(users_train)
# users_test = np.array(users_test)
# labels_train = np.array(labels_train)
# labels_test = np.array(labels_test)

# ###########################################################################
# # Create model.
# ###########################################################################

# model = Sequential()
# model.add(Dense(units=32, activation='relu', input_shape=(30, None, None, 4)))
# model.add(Dense(units=1, activation='sigmoid'))


# model.compile(loss='binary_crossentropy',
#                 optimizer='rmsprop',
#                 metrics=['binary_accuracy'])


# train_data = users_train[0].tolist()
# train_data = np.asarray(train_data)

# model.fit(train_data, labels_train[0])


# #####################################################
# # Input is a 3D array.
# #   x = 40 signatures
# #   y = Unknown number of records per signature.
# #   z = 4 features per record (x, y, time, button).
# #



# # model.add(Dense(units=32, activation='relu', input_shape=(40, None, 4)))
# # model.add(Dense(units=1, activation='sigmoid'))

# # model.compile(loss='binary_crossentropy',
# #                 optimizer='rmsprop',
# #                 metrics=['binary_accuracy'])

# # model.fit(np.array(users[0].tolist()), np.array(labels[0].tolist()), epochs=100, batch_size=30)

# # loss_and_metrics = model.evaluate(features_test, labels_test, batch_size=10)
# # print(loss_and_metrics)

# https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html