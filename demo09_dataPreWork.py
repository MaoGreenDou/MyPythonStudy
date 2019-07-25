#-*- utf-8 -*-


import requests
import re
import pandas as pd
import json
import numpy as np
from datetime import date


##  1 获取道指股票成分并且存入到一个DataFrame中去
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


dji_list = retrieve_dji_list()
djidf = pd.DataFrame(dji_list,columns=['一','二','三'])
print(djidf)

## 2 获取美国运通公司历史股票信息



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
print(quotesdf)



## 3 对数据进行一些操作之前的准备

cols = ['code','name','lasttrade']    #自定义djidf的列索引
djidf.columns = cols

quotesdf.index = range(1,len(quotes)+1)    #自定义quotesdf的行索引

dates = pd.date_range('20170520',periods=7)    #生成一个时间序列
datesdf = pd.DataFrame(np.random.randn(7,3),index=dates,columns=list('ABC'))

## 4 line_52 && line_53 自定义了quotesdf的行序列