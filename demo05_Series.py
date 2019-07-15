#-*- utf-8 -*-
import pandas as pd
from pandas import Series
import numpy as np

# Series是一种类似于字典的数据结构，但是比字典拥有更强大的功能。
# 它是一种定长有序的数据结构
# 并且它的key和value是相互独立的

##1 Series的构造

aSer = pd.Series([1,2.0,'a'])

bSer = pd.Series([1,20.0,'a'],index=['one','two','three'])

aSer[2] = 3
aSer[0] = 1
aSer[1] = 2

aSer*2

# np.exp(aSer)   为什么会报错？


cSer = pd.Series([3,5,6])
np.exp(cSer)


## 2 Series的用途之一：数据对齐

dt = dict(wang=3000,li=3000,zhao=1000)
id = ['wang','li','zhao','sun']

ser = pd.Series(dt,index=id)    #实际上相当于改变了原来字典的key和数据类型

pd.isnull(ser)

#在算术运算中自动对齐不同索引的数据

dt1 = dict(ma=32000,wang=31000)
dt.update(dt1)
ser1 = pd.Series(dt)
ser1+ser

## 3 Series的name属性

ser1.name = 'wage'
ser1.index.name = 'staff_name'


##### 仍存在的问题：注释掉的line_22
##### 原因：line_22中的每个元素的数据类型是str类型