#Draws Title for the graph using matplotlib

import matplotlib.pyplot as plt


x = [1, 2, 3]
y = [5, 7, 4]

plt.plot(x, y)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('This is a Title')
plt.show()
