#Draws Legends using matplotlib

import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]
x1 = [1, 2, 3]
y1 = [10, 14, 12]

plt.plot(x, y, label='First Line')
plt.plot(x1, y1, label='Second Line')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('This is a Title')
plt.legend()
plt.show()
