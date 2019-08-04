__author__ = 'MaoDou'
__date__ = '2019/8/4 11:07'
import requests
import re
import pandas as pd
import json
import numpy as np
from datetime import date
import time
import matplotlib.pyplot as plt
import pylab as pb

def retrieve_dji_list():
    try:
        r = requests.get('https://money.cnn.com/data/dow30/')
    except ConnectionError as err:
        print(err)
    search_pattern = re.compile(
        'class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    dji_list = []
    for item in dji_list_in_text:
        dji_list.append([item[0], item[1], float(item[2])])
    return dji_list


def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    try:
        r = requests.get(url)
    except ConnectionError as err:
        print(err)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return [item for item in quotes if not 'type' in item]


quotes = retrieve_quotes_historical('IBM')    #获取IBM公司股票信息
list1 = []
for i in range(len(quotes)):
    x = date.fromtimestamp(quotes[i]['date'])
    y = date.strftime(x, '%Y-%m-%d')
    list1.append(y)
quotesdf_ori = pd.DataFrame(quotes, index=list1)
quotesdf = quotesdf_ori.drop(['date'], axis=1)

dji_list = retrieve_dji_list()
djidf = pd.DataFrame(dji_list,columns=['一','二','三'])



tempList = []          #增加一列表示月份
for i in range(len(quotesdf)):
    temp = time.strptime(quotesdf.index[i], "%Y-%m-%d")
    tempList.append(temp.tm_mon)

tempList
quotesdf['month'] = tempList


quotes2 = retrieve_quotes_historical('INTC')    #获取intel公司股票信息
list2 = []
for i in range(len(quotes2)):
    x = date.fromtimestamp(quotes2[i]['date'])
    y = date.strftime(x, '%Y-%m-%d')
    list2.append(y)
quotesdf_ori2 = pd.DataFrame(quotes2, index=list2)
quotesdf2 = quotesdf_ori2.drop(['date'], axis=1)


tempList = []          #增加一列表示月份
for i in range(len(quotesdf)):
    temp = time.strptime(quotesdf.index[i], "%Y-%m-%d")
    tempList.append(temp.tm_mon)

tempList
quotesdf2['month'] = tempList



####绘制IBM公司和Intel公司收盘价的月平均值
dIBM = quotesdf.groupby('month').close.mean()
x_IBM = dIBM.index
x_IBM
y_IBM = dIBM.values
dIntel = quotesdf2.groupby('month').close.mean()
x_Intel = dIntel.index
y_Intel = dIntel.values

plt.subplot(121)
plt.plot(x_IBM,y_IBM,color='r',label='IBM')
plt.legend(loc='upper left')
plt.subplot(122)
plt.plot(x_Intel,y_Intel,color='blue',label='Intel')
plt.legend(loc='upper left')
plt.show()


