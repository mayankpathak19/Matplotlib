# Draws Pie Charts using matplotlib

import matplotlib.pyplot as plt


slices = [7, 2, 2, 13]
pieces = ['stack1', 'stack2', 'stack3', 'stack4']

plt.pie(slices, labels=pieces, colors=['#FF0000', '#00FF00', '#0000FF', '#FFFFFF'], startangle=90, shadow=True, explode=(0, 0.1, 0, 0), autopct='%1.1f%%')
plt.title('This is a Title')
plt.show()
