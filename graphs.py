
###########################################################################
# Import libraries.
###########################################################################
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('./Task2/Cleaning/Data/clean_user1.csv')

data = data.loc[data['signature'] == 1]

plt.plot(data['time'][0], data['x'][0])
plt.plot(data['time'][0], data['y'][0])
plt.plot(data['time'][0], data['button'][0])
plt.plot(data['time'][0], data['azimuth'][0])
plt.plot(data['time'][0], data['altitude'][0])
plt.plot(data['time'][0], data['pressure'][0])
plt.show()
