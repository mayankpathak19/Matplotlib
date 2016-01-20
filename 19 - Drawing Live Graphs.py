# Drawing live graphs
# If the data reservoir is getting updated regularly then use this for graphing in real time.

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.style as style


style.use('fivethirtyeight')
figure = plt.figure()
axes1 = figure.add_subplot(1, 1, 1)


def animate(i):
    graph_data = open('example.txt', 'r').read()
    lines = graph_data.split('\n')
    x = []
    y = []
    for line in lines:
        alpha, beta = line.split(',')
        x.append(alpha)
        y.append(beta)
    axes1.clear()
    axes1.plot(x, y)

ani = animation.FuncAnimation(figure, animate, interval=1000)
plt.show()
