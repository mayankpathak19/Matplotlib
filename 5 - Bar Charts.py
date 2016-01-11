import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [6, 7, 8, 2, 4]
x1 = [1, 3, 5, 7, 9]
y1 = [7, 8, 2, 4, 2]

plt.bar(x, y, label='First Graph', color='#FF0000')
plt.bar(x1, y1, label='Second Graph', color='#00FFFF')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('This is a Title')
plt.legend()
plt.show()
