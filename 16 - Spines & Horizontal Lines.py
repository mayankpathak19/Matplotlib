# Spines and Horizontal Lines.

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import urllib


def convert_date(date_format, encoding='utf-8'):
    string_converter = mdates.strpdate2num(date_format)

    def bytes_converter(b):
        s = b.decode(encoding)
        return string_converter(s)
    return bytes_converter


def graph_data(stock):
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=10y/csv'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
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
    ax1.plot_date(date, close_price, '-', label='Price')
    ax1.plot([], [], linewidth=5, label='Loss', color='#FF0000', alpha=0.5)
    ax1.plot([], [], linewidth=5, label='Profit', color='#00FF00', alpha=0.5)
    ax1.axhline(close_price[0], color='#000000', linewidth=5)
    ax1.fill_between(date, close_price, close_price[0], alpha=0.3, where=(close_price > close_price[0]),
                     facecolor='#00FF00')
    ax1.fill_between(date, close_price, close_price[0], alpha=0.3, where=(close_price < close_price[0]),
                     facecolor='#FF0000')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    for label in ax1.yaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True)
    ax1.xaxis.label.set_color('#FF0000')
    ax1.yaxis.label.set_color('#FFFF00')
    ax1.set_yticks([0, 25, 50, 75])
    ax1.spines['left'].set_color('#00FFFF')
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.spines['left'].set_linewidth(5)
    ax1.tick_params(axis='x', colors='#F06215')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.2, right=0.94, top=0.9, wspace=0.2, hspace=0)
    plt.show()


name = input('Enter the name of stock\n')
graph_data(name)
