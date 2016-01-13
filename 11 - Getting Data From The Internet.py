# Getting data from the internet

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
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source_code = source_code.split('\n')
    for line in split_source_code:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line:
                stock_data.append(line)
    date, close_price, high_price, low_price, open_price, stock_volume = np.loadtxt(stock_data, delimiter=',',
                                                                                    unpack=True, converters={
            0: convert_date('%Y%m%d')})
    plt.plot_date(date, close_price)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('This is a Title')
    plt.legend()
    plt.show()

name = raw_input('Enter the name of stock\n')
graph_data(name)
