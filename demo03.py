#-*- utf-8 -*-

## 1 字符串操作

#字符串的格式化输出

a = 3
b = 3.2
c = 'Hello World!'
print('Winter is coming {2:s} {0:d} {1:f}'.format(a,b,c))

#关于字符串的操作函数有很多，通过dir命令和help命令进行查看

#  单引号，双引号，三单引号的区别和用处，还有原始字符标识r/R

## 2 列表，列表的相关操作，列表解析，生成器

list = [(x**2,y**2) for x in range(10) for y in range(10) if x%2==0 and y%2==0]
for item in list:
    print(item)

g = ((x**2,y**2) for x in range(10) for y in range(10) if x%2==0 and y%2==0)      #想要得到庞大的数据，又想让它占用空间少，那就用生成器！

## 3 元组
#使用1.元组中的元素不可更改

list = [x for x in range(10)]
tuple = (0,1,2,3,4,5,6,7,8,9)

reversed(list)  # is ok
reversed(tuple)  # is ok

list.reverse()   #is ok
# tuple.reverse()  is not ok

#使用2. 可以用作函数参数：可变长的位置参数

def fun1(args1,*args2):
    print(args1)
    print(args2)

fun1('Hello',' winter',' is ',' coming')

#使用3. 可用作返回值

def fun2():
    return 1,2,3

r = fun2()
print(r[1:])

##  4 字典

#字典的生成

# 1 直接生成

r = {'wang':3000,'li':2000,'zhao':10000}

# 2 通过dict间接生成  （只要序列中的元素有明确的映射关系即可）

list = [('wang',3000),('li',2000),('zhao',1000)]
r = dict(list)

list = (('wang',3000),('li',2000),('zhao',1000))
r = dict(list)

r = dict(wang=3000,li=2000,zhao=3000)

# 3 字典的默认value值的设置

r = {}.fromkeys(('wang','li','zhao'),3000)

# 4 字典的打包

list1 = ['wang','li','zhao']
list2 = [3000,2000,1000]
r = zip(list1,list2)

## 字典的使用

#字典元素的查找，更改，增添，删除

d = {'wang':3000,'li':2000,'zhao':1000}

d['wang']
d.get('wang')

d['wang'] = 3500

d['sun'] = 3600

'ma' in d

del d['wang']

#字典元素的遍历

d.values()
d.keys()
d.items()

#字典元素的更新

d1 = dict(wang=3000,li=15000,ma=3320)
d.update(d1)

#字典的用处
#1 用作JASON格式（轻量性的数据交换格式）
#2 用作搜索引擎的关键词查询
#3 用作可变长的关键字参数

def foo(args1,*args2,**args3):
    print(args1)
    print(args2)
    print(args3)

foo('Hello', ' this', ' is', ' winterfell', a1=3000, a2=3000, a3=5000)