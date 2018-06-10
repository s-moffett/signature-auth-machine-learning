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
def load_task_1():
    
    print('Loading data...')

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
        user_signatures.to_csv('./Redux/Data/Cleaning/clean_user' + str(user) + '.csv')   

    return


if __name__ == '__main__':
    load_task_1()
