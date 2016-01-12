# Getting data from a file

import matplotlib.pyplot as plt
import csv


x = []
y = []

with open('example.txt', 'r') as csv_file:
    plots = csv.reader(csv_file, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
plt.plot(x, y, label='First Graph')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('This is a Title')
plt.show()
