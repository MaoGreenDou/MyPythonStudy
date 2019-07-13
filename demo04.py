#-*- utf-8 -*-

import  numpy as np
import time
import math

## 1 ndarry的四种创建方法

#1
array = np.array([1,2,3])
print(array)
array = np.array([(1,2,3),(4,5,6),(7,8,9)])
print(array)
#2
array = np.arange(1,10,2)
print(array)
#3
array = np.random.random((2,2))
print(array)
#4
array = np.linspace(1,10,10,endpoint=False)
print(array)
## 2 特殊矩阵的创建方法

array = np.ones([2,2])      #里面是中括号还是圆括号都可以，下同理
print(array)
array = np.zeros([2,2])
print(array)
array = np.fromfunction(lambda x,y:(x+1)*(y+1),[9,9])
print(array)

## 3 矩阵的一些属性

array = np.ones((3,4))

array.size
array.shape
array.ndim
array.dtype
array.itemsize

## 4 矩阵中元素的访问

array = np.array([(1,2,3),(4,5,6),(7,8,9)])

print(array[2][2])

print(array[2])

print(array[0:2])

print(array[:,[1,2]])

print(array[1,[1,2]])

for item in array:
    print(item)

## 5 矩阵中元素的操作

array = np.array([(1,2),(3,4),(5,6)])

bArray = array.reshape(2,3)

array.resize(2,3)

array = np.array([1,2,3])
bArray = np.array([4,5,6])
cArray = np.vstack((array,bArray))
cArray = np.hstack((array,bArray))

## 6 矩阵的运算

array = np.ones([2,3])
array1 = np.array([(1,2,3),(4,5,6)])

array2 = array + array1
array3 = array * array1      #属于点乘运算
array = 10 * np.ones([2,2])

a = np.array([1,2,3])
b = np.array([(1,2,3),(4,5,6)])

a + b    #广播的思想

## 7 一些统计方法

array = np.array([(1,2,3),(4,5,6),(7,8,9)])

array.sum();
array.sum(axis=0)
array.sum(axis=1)

array.min()
array.argmax()
array.var()
array.std()

## 8 线性代数运算

array = np.array([(1,2,3),(4,5,6),(7,8,9)])
print("行列式",np.linalg.det(array))
print("逆矩阵",np.linalg.inv(array))
array1 = np.dot(array,array)        #内积

## 9 numpy中的通用函数（C语言级别的实现，速度较快相对于math模块来说，用来处理大量数据）

x = np.arange(0,10000,0.01)
t_m1 = time.clock()
for i,t in enumerate(x):
    x[i] = math.pow(math.sin(t),2)
t_m2 = time.clock()

y = np.arange(0,10000,0.01)
t_n1 = time.clock()
y = np.power(np.sin(y),2)
t_n2 = time.clock()

print("MATH:",t_m2 - t_m1)
print("NUMPY:",t_n2-t_n1)



