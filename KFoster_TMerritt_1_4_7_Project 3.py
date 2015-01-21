import matplotlib.pyplot as plt
import os.path  
import numpy as np



directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'images.jpeg')
img = plt.imread(filename)
fig, ax = plt.subplots(1, 1)
fig.show()