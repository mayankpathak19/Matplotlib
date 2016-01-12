# Getting data from a file

import matplotlib.pyplot as plt
import numpy as np


x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)
plt.plot(x, y, label='First Graph')
plt.plot(x, y)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('This is a Title')
plt.show()
