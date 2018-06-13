"""
    Runs entire training pipeline.
"""

###########################################################################
# Import local functions.
###########################################################################

import cleaning
import features
import training

###########################################################################
# Pipeline.
###########################################################################

# Load data into CSV files.
cleaning.load_task_1()

# Clean data.
cleaning.clean_task_1()

# Create features.
features.features_task_1()

# Train models.
training.train_task_1_neural_net()
