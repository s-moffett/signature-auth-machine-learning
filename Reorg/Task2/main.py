"""
  Runs the project.
"""

# Import local methods.
import loading
import cleaning
import features
import training

# Load raw data into datasets.
loading.load()

# Clean data.
cleaning.clean()

# Create features.
features.create_features()

# Train neural network.
# training.train_neural_network()

# Train logistic regression.
# training.train_logistic_regression()
