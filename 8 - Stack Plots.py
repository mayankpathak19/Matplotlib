# Draws Stack Plots using matplotlib

import matplotlib.pyplot as plt


x = [alpha for alpha in range(1, 6)]
stack1 = [7, 8, 6, 11, 7]
stack2 = [2, 3, 4, 3, 2]
stack3 = [7, 8, 7, 2, 2]
stack4 = [8, 5, 7, 8, 13]

plt.plot([], [], color='#FF0000', label='First Graph', linewidth=5)
plt.plot([], [], color='#00FF00', label='Second Graph', linewidth=5)
plt.plot([], [], color='#0000FF', label='Third Graph', linewidth=5)
plt.plot([], [], color='#000000', label='Fourth Graph', linewidth=5)
plt.stackplot(x, stack1, stack2, stack3, stack4, colors=['#FF0000', '#00FF00', '#0000FF', '#000000'])
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('This is a Title')
plt.legend()
plt.show()
