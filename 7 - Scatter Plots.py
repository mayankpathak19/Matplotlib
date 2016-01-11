# Draws Scatter Plots using matplotlib

import matplotlib.pyplot as plt


x = [alpha for alpha in range(1, 9)]
y = [5, 2, 4, 2, 1, 4, 5, 2]

plt.scatter(x, y, label='First Graph', color='#000000', marker='*', s=10)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('This is a Title')
plt.legend()
plt.show()
