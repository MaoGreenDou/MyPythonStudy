#-*- utf-8 -*-

import pandas as pd
import numpy as np

## 1 DataFrame的初始化

info = np.array([('wang',3000),('chai',1000),('yang',5000)])

df = pd.DataFrame(info,columns=['name','wage'],index=['A','B','C'])

print(df)

## 2 DF中数据的访问及修改

df.values
df.columns
df.index

df.values[1] = ['ma',32000]

df['name']
df.wage

df.iloc[:2,1]

df['name'] = 'userName'

# del df['wage']    删除一列

## 3 Data中的统计功能

df.wage.min()  #先获得一个Series对象，返回值是str类型的数据

df[df.wage>='5000']   #注意是str类型的5000