#-*- coding:utf-8 -*-

import numpy as np
import tushare as ts
import time
from pandas import Series

d1 = ts.get_hist_data('600036',start='2018-06-01',end='2018-12-31')

print(d1.columns)

d2 = d1.drop(['price_change', 'p_change',
       'ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20'],axis=1)

d3 = d2.sort_values(by=['date'])

print(d3[d3.volume==d3.volume.max()])

print(d3[d3.volume==d3.volume.min()])

print(d3[d3.volume>=10e5])

# print(d3[d3.close>d3.open].value_counts())  #错
print(d3[d3.close>d3.open].count())

ay = np.sign(np.diff(d3.open))
print(ay)

tempList = []
for i in range(len(d3)):
    temp = time.strptime(d3.index[i],"%Y-%m-%d")
    tempList.append(temp.tm_mon)
d3['month'] = tempList
print(d3.groupby('month').close.mean())


####Tips:
#区分：cout（），value_counts（）