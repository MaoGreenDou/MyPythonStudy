# -*- coding:utf-8 -*-

#注意事项
# 1. Pycharm中的编码方式以及.py文件的开头语句
# 2. Pycharm的一些配置 eg：快捷键，解释器，虚拟机等
# 3. Pycharm如何打开shell命令窗口
# 4. Pycharm与git和github/githubdesk的配合使用 eg：从github中clone项目，上传项目到github等等（如何上传到指定repository？）

# 1 first program

print('Hello World!')

# float data
PI = 3.14159
pi = 3.14159
PI is pi

id(PI)
id(pi)

# 2 integer data

p = 3
q = 3
q is p

id(q)
id(p)

# 3 big integer data

a = 257
b = 257

a is b

id(a)
id(b)

# 4 string data

x = 'Hello World!'
y = 'Hello World'

x is y
id(x)
id(y)


# 5 数据类型：新增的：单引号/双引号/三引号字符串，元组，字典

data={'cos':'cos_value','sin':'sin_value'}
print(data['cos'])

# 6 运算符操作


x = int(input("Input x: "))       #输入语句
y = int(input("Input y: "))

print("x+y =", x + y)
print("x-y =", x - y)
print("x*y =", x * y)
print("x/y =", x / y)
print("x//y =", x // y)

# 7 r/R 运算符

print(r'this is a test\n')
print(R'this is a test\n')
print('this is a test\n')
print('this is a test')
print('this is a test')   # print语句 默认加一个换行符

# 8 输入输出语句小练习

firstname = input('请输入你的姓')
secondname = input('请输入你的名')
print('你的姓是',firstname)
print('你的名字',secondname)

# 9 python当中的 包  库 模块 之间的关系 以及两种导入方式

# 10 条件结构

a = 1
b = 2
c = 3
d = 1

if a>b:
    print('a>b')
elif b>c:
    print('b>c')
elif c<d:
    print('c<d')
else:
    print('a = d')

# 11 range 函数

list(range(10))

print(range(10))      #这输出的是啥

list = range(5,10)
print(list)          #同上，这输出的是啥

list = range(5,10,2)
print(list)

print(list[2])

# 12 while循环，for循环，列表解析，生成器

j = 0;
while j<10:
    print(j)
    j += 1


for i in range(10):
    print(i)


[i for i in range(10)]
[i+1 for i in range(10) if i%2 == 0]

(i for i in range(10) if i%2 == 0)

# 13 循环与break continue else的运用

for i in range(10):
    if i<5:
        print("i的值",i)
        break

print("跳出循环i的值",i)        # python中break跳出for循环，i的值不再+1

j = 0

while j<10:
    j += 1
else:
    print("while与else的连用",j)   # python中else可以与while一起配合使用



# C 代码
# #include <stdio.h>
# #include <stdlib.h>
#
# int main()
# {
#     int j = 0;
#     for(;j<10;j++)
#     {
#         if(j==5)
#         {
#           break;
#         }
#     }
#     printf("J的值%d",j);
#     return 0;
# }
#


# 14 函数：函数的定义；描述；位置参数；默认参数；关键字参数；lambda函数

def fun1(x,y=10):
    '输出x，y的值'
    print('x的值',x,'y的值',y)


fun1(1)     # 位置参数；默认参数
fun1(y = 10,x = 2)    #关键字参数

r = lambda x,y : x + y
print(r(3,10))      #lambda函数


# 15 递归

def sum(x):
    '递归求和函数'
    if (x == 1) or (x == 0):
        return x
    else:
        return x + sum(x-1)

print(sum(5))

# 16 变量的作用域   全局变量 和 局部变量

str = 'Hello'
def fun2():
    '不改变全局变量情况下的全局变量和局部变量的运算'
    print(str+' World!')

fun2()


a = 10

def fun3(x):
    '改变全局变量情况下的全局变量和局部变量的运算'

    global a                   #不是字符串的全局变量的声明要放在函数的最前面
    print('局部变量x的值是',x)
    print('全局变量a改之前的值是',a)

    a = 3
    print('全局变量a改之后的值是',a)
    print('a + x = ',a+x)


fun3(100)
print('退出函数fun3的a的值',a)



#  lesson_2   2019_7_8_one

# 17 Python中的常用标准库函数


# import math
# import os
# import random
# import datetime    etc..


# 18 Python的异常处理机制

#形式一

try:
    x = int(input('input a value'))
    y = int(input('input another value'))
    print(r'x/y = ',x/y)

except ZeroDivisionError:
    print('出现除零错误')
except ValueError:
    print('出现值错误')


#形式二

try:
    x = int(input('input a value'))
    y = int(input('input another value'))
    print(r'x/y = ',x/y)

except Exception as err:
    print(err)


#形式三 与 else 配合使用


try:
    x = int(input('input a value'))
    y = int(input('input another value'))
    print(r'x/y = ',x/y)

except Exception as err:
    print(err)

else:
    print('没有捕捉到异常')


#形式四 与 final 配合使用

try:
    x = int(input('input a value'))
    y = int(input('input another value'))
    print(r'x/y = ',x/y)

except Exception as err:
    print(err)

finally:
    print('不管捕捉没捕捉到异常，都要执行该语句')


#形式五 与 循环结构和break配合使用（注意break放置的位置）


#形式六 上下文管理器（常配合文件操作和数据库管理操作一起使用）

# with open('text.txt') as f:
#     for res in f:
#         print(res,end = '')

# 19 Python 本地数据获取

#文件操作流程
#1.打开文件（路径，打开方式，缓冲方式，编码方式等等参数）
#2.操作文件（读文件，写文件，追加文件，改变文件指针等，还有一些f_obj的方法可以使用）
#3.关闭文件
#注：上述操作可以放在上下文管理器中进行（文件打开，操作，默认关闭）

#例：

with open(r'E:\PythonProject\lesson_19_7_7\test1.txt','w+') as f:          #还有其他默认参数，缓冲方式-1、0、>=1
    f.write('Hello World!')
    f.seek(0,0)                                                           #有默认参数 0 1 2
    print(f.read(5))
    print(f.read())

with open(r'E:\PythonProject\lesson_19_7_7\test1.txt','r') as f1:
    with open(r'E:\PythonProject\lesson_19_7_7\test2.txt','w') as f2:
        str = f1.readlines()
        f2.writelines(str)


