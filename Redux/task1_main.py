"""
    Runs entire training pipeline.
"""

###########################################################################
# Import local functions.
###########################################################################

import cleaning

###########################################################################
# Pipeline.
###########################################################################

# # Load data into CSV files.
cleaning.load_task_1()

# Clean data
cleaning.clean_task_1()

