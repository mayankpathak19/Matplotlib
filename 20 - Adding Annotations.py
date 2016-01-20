# Adding Annotations

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
from matplotlib import style
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
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=1m/csv'
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
    x = 0
    y = len(date)
    ohlc = []
    while x < y:
        data = date[x], close_price[x], high_price[x], low_price[x], open_price[x], stock_volume[x]
        ohlc.append(data)
        x += 1
    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#77D879', colordown='#DB3F3F')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    for label in ax1.yaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.grid(True)
    ax1.annotate('Big News!', (date[8], high_price[11]), xytext=(0.8, 0.9), textcoords='axes fraction',
                 arrowprops=dict(facecolor='grey', color='grey'))
    font_dict = {'family': 'serif', 'color': 'darkred', 'size': 15}
    ax1.text(date[10], close_price[1], 'EBAY Prices', fontdict=font_dict)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.2, right=0.94, top=0.9, wspace=0.2, hspace=0)
    plt.show()


style.use('fivethirtyeight')
name = input('Enter the name of stock\n')
graph_data(name)
