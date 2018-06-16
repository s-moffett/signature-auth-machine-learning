
###########################################################################
# Import libraries.
###########################################################################
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

# # Plot raw sample.
# data = pd.read_csv('../../Dataset2/user1.csv')
# samples = []
# for sig in range(1, 41):
#   samples.append(data.loc[data['signature'] == sig])

# plt.plot(samples[0]['time'], samples[0]['x'])
# plt.plot(samples[0]['time'], samples[0]['y'])
# plt.plot(samples[0]['time'], samples[0]['azimuth'])
# plt.plot(samples[0]['time'], samples[0]['altitude'])
# plt.plot(samples[0]['time'], samples[0]['pressure'])

# plt.legend(['X', 'Y', 'Azimuth', 'Altitude', 'Pressure'])
# plt.show()

# # Plot cleaned sample.
# data = pd.read_csv('./Task2/Cleaning/Data/clean_user8.csv')
# samples = []
# for sig in range(1, 41):
#   samples.append(data.loc[data['signature'] == sig])

# plt.plot(samples[0]['time'], samples[0]['x'])
# plt.plot(samples[0]['time'], samples[0]['y'])
# plt.plot(samples[0]['time'], samples[0]['azimuth'])
# plt.plot(samples[0]['time'], samples[0]['altitude'])
# plt.plot(samples[0]['time'], samples[0]['pressure'])
# plt.show()


# Plot cleaned sample.
data = pd.read_csv('./Task2/Features/Data/Sampled/features_user8.csv')
samples = []
for sig in range(1, 41):
  samples.append(data.loc[data['signature'] == sig])

plt.plot(samples[0]['time'], samples[0]['x'])
plt.plot(samples[0]['time'], samples[0]['y'])
plt.plot(samples[0]['time'], samples[0]['azimuth'])
plt.plot(samples[0]['time'], samples[0]['altitude'])
plt.plot(samples[0]['time'], samples[0]['pressure'])
plt.show()



# # Plot signatures.
# for sample in range(0, 40):
#   plt.subplot(20, 2, sample + 1)
#   plt.plot(samples[sample]['x'], samples[sample]['y'])
# plt.show()



