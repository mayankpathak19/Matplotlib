# Handling UNIX time

import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import urllib


def graph_data(stock):
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=10d/csv'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source_code = source_code.split('\n')
    for line in split_source_code:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line:
                stock_data.append(line)
    date, close_price, high_price, low_price, open_price, stock_volume = np.loadtxt(stock_data, delimiter=',',
                                                                                    unpack=True)
    date_convertor = np.vectorize(dt.datetime.fromtimestamp)
    date = date_convertor(date)
    ax1.plot_date(date, close_price, '-', label='Price')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    for label in ax1.yaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('This is a Title')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.2, right=0.94, top=0.9, wspace=0.2, hspace=0)
    plt.show()


name = input('Enter the name of stock\n')
graph_data(name)
