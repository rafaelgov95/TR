import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
labs = 500

grey_height=28 + 4 * np.random.rand(greyhounds)
labs_height= 24 + 4 * np.random.rand(greyhounds)
plt.hist([grey_height,labs_height])
plt.show