#-*- utf-8 -*-

# 收集 整理 描述 分析

import requests
import re
import pandas as pd
import json

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
        quotes = json.loads(m[0])  # m = ['[{...},{...},...]']
        quotes = quotes[::-1]  # 原先数据为date最新的在最前面
    return [item for item in quotes if not 'type' in item]


quotes = retrieve_quotes_historical('AXP')
quotesdf = pd.DataFrame(quotes)
# quotesdf = quotesdf_ori.drop(['adjclose'], axis = 1)  可用本语句删除adjclose列
print(quotesdf)


## 3 直接下载csv，json格式文档，然后通过pd中的相关函数对文档进行操作
# import pandas as pd
# quotesdf = pd.read_csv('axp.csv')
# print(quotesdf)



## 4 通过网站提供的API进行数据获取 (豆瓣API现在已不提供访问)

# r = requests.get('https://api.douban.com/v2/book/10084336')
# r.text
# Out[8]: '{"msg":"invalid_apikey","code":104,"request":"GET \\/v2\\/book\\/10084336"}'