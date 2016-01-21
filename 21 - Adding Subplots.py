# Adding Subplots

import random
import matplotlib.pyplot as plt
import matplotlib.style as style


style.use('fivethirtyeight')
figure = plt.figure()


def create_plots():
    x_value = []
    y_value = []
    for i in range(10):
        alpha = i
        beta = random.randrange(10)
        x_value.append(alpha)
        y_value.append(beta)
    return x_value, y_value

axes1 = figure.add_subplot(211)
axes2 = figure.add_subplot(222)
axes3 = figure.add_subplot(212)
x, y = create_plots()
axes1.plot(x, y)
x, y = create_plots()
axes2.plot(x, y)
x, y = create_plots()
axes3.plot(x, y)
plt.show()
