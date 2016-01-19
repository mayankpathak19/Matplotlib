# Working with Styles
# To view the current availbe styles in Matplotlib type in print(plt.styles.availble).
# To use a predefined style firstly do from matplotlib import style, then type in style.use(style name).
# To add your own style to the predefined list or to edit a predefined style
# first find out the place where matplotlib is installed by typing print(plt.__file__).
# In that directory go in 'mpl-data/stylelib/'.
# The above directory contains the availble styles open and edit it or create a new one with the same extension.

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib import style
import numpy as np
import urllib as url


def convert_date(date_format, encoding='utf-8'):
    string_converter = mdates.strpdate2num(date_format)

    def bytes_converter(b):
        s = b.decode(encoding)
        return string_converter(s)

    return bytes_converter


def graph_data(stock):
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=1m/csv'
    source_code = url.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source_code = source_code.split('\n')
    for line in split_source_code:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line:
                stock_data.append(line)
    date, close_price, high_price, low_price, open_price, stock_volume = np.loadtxt(stock_data,
                                                                                    delimiter=',',
                                                                                    unpack=True,
                                                                                    converters={
                                                                                        0: convert_date('%Y%m%d')})
    ax1.plot(date, close_price)
    ax1.plot(date, open_price)
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    for label in ax1.yaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.grid(True)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.2, right=0.94, top=0.9, wspace=0.2, hspace=0)
    plt.show()


style.use('fivethirtyeight')
name = input('Enter the name of stock\n')
graph_data(name)
