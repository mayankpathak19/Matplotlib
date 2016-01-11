# Draws Histograms using matplotlib

import matplotlib.pyplot as plt

y = [22, 55, 62, 45, 21, 22, 34, 42, 42,4, 99, 102, 110, 120, 121, 122, 130, 111, 115, 112, 80, 75, 65, 54, 44, 43, 42, 48]
x =[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(y, x, histtype='bar', rwidth=0.8, label='First Graph')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('This is a Title')
plt.legend()
plt.show()
