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
print(quotesdf_ori)
quotesdf = quotesdf_ori.drop(['date'], axis=1)
print(quotesdf)



## 3 对数据进行一些操作之前的准备

cols = ['code','name','lasttrade']    #自定义djidf的列索引
djidf.columns = cols

# quotesdf.index = range(1,len(quotes)+1)    #自定义quotesdf的行索引

dates = pd.date_range('20170520',periods=7)    #生成一个时间序列
datesdf = pd.DataFrame(np.random.randn(7,3),index=dates,columns=list('ABC'))

## 4 line_52 && line_53 自定义了quotesdf的行序列



##下面进行数据显示环节
##可以利用之前提到的切片操作
##也可以用df提供的函数

djidf.index
print(list(djidf.index))    #查看列索引

djidf.columns
print(list(djidf.columns))    #查看行索引

print(djidf.values)    #查看数据内容（不包括行索引和列索引）

print(djidf.describe)    #查看对数据的描述

djidf.lasttrade    #查看指定索引的数据内容，数据标签，数据类型

djidf.head(5)
djidf[:5]

djidf.tail(5)
djidf[-5:]

djidf.lasttrade

djidf.size    #同下，不包括索引所占行和列

djidf.shape



#### 暂时对切片操作的理解
#切片操作有两个冒号，三个数字
#序列有正负两组索引

#第一个数字代表起始位置：默认为0
#第二个数字代表结束为止：默认为序列长加一
#第三个数字代表步长：默认为1

#当步长为正时：只能从左往右遍历（对索引的正负无要求）
#当步长为负时：只能从右往左遍历（对索引的正负无要求）


##数据的选择

#数据的选择包括如下：
#选择一行
#选择一列
#选择一片区域
#选择满足条件的部分

## 1 行操作
 #可以使用切片的部分操作（不支持全部的切片操作）
quotesdf['2019-07-30':'2019-08-01']

## 2 列操作
 #不支持切片操作
 #可以使用标签访问
quotesdf.open

## 3 loc操作 loc[行，列]
#注：这里最外层中括号里的行和列指的都是标签，不要和切片操作混淆

djidf.loc[1:5,['code','lasttrade']]

djidf.loc[:,['code','name','lasttrade']]

djidf.loc[[1,5],['code','lasttrade']]


 #特别的如果要选择某一个值，可以用at进行操作

djidf.loc[1,'lasttrade']
djidf.at[1,'lasttrade']

## 4 iloc操作
#注： 这里的数字指的是物理位置，和切片操作相同

djidf.iloc[0:6,[0,2]]

djidf.iloc[[0,2],[0,2]]

djidf.iloc[-5:,[0,2]]


## 5 选择满足条件的区域
#直接在中括号里加上条件判断即可

djidf[(djidf.lasttrade>=200)&(djidf.lasttrade<=300)]    #注意数据类型