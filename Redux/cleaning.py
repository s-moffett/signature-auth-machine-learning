"""
    Cleans data.
"""

###########################################################################
# Import libraries.
###########################################################################
import pandas as pd
import numpy as np

# Disable pandas warnings
pd.options.mode.chained_assignment = None

###########################################################################
# Load data from txt files.
###########################################################################
def load_task_1():
    
    print('Loading data from TXTs into CSVs...')

    # Load each user's signatures into a single user dataframe.
    for user in range(1, 41):

        # Empty user dataframe.
        user_signatures = pd.DataFrame(columns=['x', 'y', 'time', 'button'])
        
        for sig in range(1, 41):
        
            # Get the signature.
            signature = pd.read_csv('./Data/CSV/Input/Task1/U' + str(user) + 'S' + str(sig) + '.TXT', sep=' ', skiprows=1, names=['x', 'y', 'time', 'button'])        

            # Add 'signature' field.
            signature['signature'] = sig

            # Add the label.
            if sig < 21:
                signature['genuine'] = 1
            else:
                signature['genuine'] = 0

            # Add signature to user dataframe.
            user_signatures = user_signatures.append(signature)

        # Output user dataframe to file.
        user_signatures.to_csv('./Redux/Data/Loading/user' + str(user) + '.csv')   

    return

###########################################################################
# Clean data.
###########################################################################
def clean_task_1():

    print('Begin cleaning...')

    for user in range(1, 41):

        print('Loading user ' + str(user) + '...')

        # Read data from CSV.
        user_dataframe = pd.read_csv('./Redux/Data/Loading/user' + str(user) + '.csv')
    
        # Separate user dataframe into separate signatures.
        signatures = []        
        for sig in range(1, 41):
            signatures.append(user_dataframe.loc[user_dataframe['signature'] == sig])

        # Max number of records in any of this user's signatures. Used to product even arrays.
        max_signature_length = 0

        print('Cleaning user ' + str(user) + '...')

        # A few looping operations.
        for sig in range(0, 40):

            # Zero x, y, and time.
            #   
            #   A signature's x, y, and time values are only meaningful
            #   relative to the min values with that signature, i.e.
            #   they should be translated to 0.
            #
            signatures[sig]['time'] = signatures[sig]['time'] - signatures[sig]['time'].min()
            signatures[sig]['x'] = signatures[sig]['x'] - signatures[sig]['x'].min()
            signatures[sig]['y'] = signatures[sig]['y'] - signatures[sig]['y'].min()

            # Find the max number of records in any signature for this user.
            #
            #   This will be used to make the user's signatures equal lengths.  
            #
            if signatures[sig]['time'].count() > max_signature_length:
                max_signature_length = signatures[sig]['time'].count()

        print('Adding records to user ' + str(user) + '...')

        # Add records to signatures so all signatures by a particular user are the same length.
        for sig in range(0, 40):

            print('\t Signature ' + str(sig))
            max_time = signatures[sig]['time'].max()
            genuine = signatures[sig]['genuine'].max()

            for i in range(0, max_signature_length - signatures[sig]['time'].count()):
                df = pd.DataFrame([[0, 0, max_time, 0, user, sig+1, genuine]], columns=['x', 'y', 'time', 'button', 'user', 'signature', 'genuine'])
                signatures[sig] = signatures[sig].append(df)
                max_time += 10

        # Combine this user's signatures into a single user dataframe.
        user_dataframe = pd.DataFrame()
        
        for sig in range(0, 40):
            user_dataframe.append(signatures[sig])

        user_dataframe.to_csv('./Redux/Data/Cleaning/clean_user' + str(user) + '.csv')

    return

###########################################################################
# For testing.
###########################################################################
if __name__ == '__main__':
    clean_task_1()
