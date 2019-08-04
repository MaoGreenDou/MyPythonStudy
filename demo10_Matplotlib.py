__author__ = 'MaoDou'
__date__ = '2019/8/3 18:50'

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


quotes = retrieve_quotes_historical('IBM')
list1 = []
for i in range(len(quotes)):
    x = date.fromtimestamp(quotes[i]['date'])
    y = date.strftime(x, '%Y-%m-%d')
    list1.append(y)
quotesdf_ori = pd.DataFrame(quotes, index=list1)
quotesdf = quotesdf_ori.drop(['date'], axis=1)

dji_list = retrieve_dji_list()
djidf = pd.DataFrame(dji_list,columns=['一','二','三'])



##绘图操作
tempList = []
for i in range(len(quotesdf)):
    temp = time.strptime(quotesdf.index[i], "%Y-%m-%d")
    tempList.append(temp.tm_mon)

tempList
quotesdf['month'] = tempList
quotesdf
d1 = quotesdf.groupby('month').close.mean()
d1.index
quotesdf['month'].value_counts()
quotesdf.groupby('month').count()
x = d1.index
x
y = d1.values
d1
y
plt.plot(x, y)

t = np.arange(1, 10, 2)
t
plt.plot(t, t, t, t + 2, t, t ** 2)
plt.plot(t, t, t, t + 2, t, t ** 2, 'o')
plt.bar(x, y)
plt.show()
import pylab as pb

pb.plot(t, 2 * t + 1)
pb.show()


##属性设置

#1
fig, (ax0, ax1) = plt.subplots(2, 1)      # 2行1列
ax0.plot(range(7), [3, 4, 7, 6, 2, 8, 9], color = 'r', marker = 'o',linewidth=3,label='line2',linestyle='-')
ax0.set_title('subplot1')    # 设置子图的标题
plt.subplots_adjust(hspace = 0.5)
ax1.plot(range(7), [5, 1, 8, 2, 6, 9, 4], color = 'green', marker = 'o')
ax1.set_title('subplot2')
plt.show()
#---------------------------------------------
#plt.plot(t,t,label='lin1')
#plt.plot(t,t,label='lin2')
#plt.legend(loc='upper left')

#2
#plt.subplot(211)
#draw
#plt.subplot(212)
#draw
#show
