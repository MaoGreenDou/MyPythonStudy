# -*- coding: utf-8 -*-
__author__ = 'MaoDou'
__date__ = '2019/8/8 18:18'

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sklearn import datasets
import seaborn as sns

sns.set_style('whitegrid')

boston = datasets.load_boston()
X = boston.data    # 506条记录，13个属性
Y = boston.target    # 房价记录MEDV


# 绘图
fig, ax = plt.subplots()
fig.set_tight_layout(True)
ax.scatter(X[:, 12], Y)    # 绘制RM-Price散点图
ax.set_title('low-income groups ~ price')
plt.xlabel('low-income groups/%')
plt.ylabel('PRICE/k')
# plt.show()

# 用线性回归模型拟合数据
# h_θ(x) = θ_0 + θ_1*x_1 + θ_2*x_2
# 其中 x_1 = X[:,12] x_2 = suqrt(X[:,12])

x_1 = np.array([X[:, 12]])
x_2 = np.array([np.sqrt(X[:, 12])])

dataX = np.hstack((x_1.T, x_2.T))  # 获得特征ndarray

# 数组转矩阵的时候默认转化为单行或者单列默认都转化为行向量

temp = np.ones([506, 1])

# 是不是加括号的都是矩阵，不加的都是数组？区分多维，单维数组和矩阵

dataX = np.hstack((temp, dataX))


# 定义假设函数
def hy(x, theta):
    'x and theta both are column vector'
    return np.dot(theta.T, x)

# 定义代价函数


def costJ(X, Y, theta, h):
    'X is feature martix,Y is target(col vector),theta is parameter(col vector),h is hypothesis '
    sum = 0
    for i in range(Y.size):
        temp = h(X[i, ].T, theta) - Y[i]
        sum += np.power(temp, 2)
    return sum[0] / 2 * (Y.size)

# 定义正规方程法


def nEuqa(X, Y):
    'X is featuer martix,Y is target(col vector)'
    temp1 = np.dot(X.T, X)
    temp2 = np.linalg.pinv(temp1)
    temp3 = np.dot(temp2, X.T)
    temp4 = np.dot(temp3, Y)
    return temp4


res = nEuqa(dataX, Y)
print(res, res.shape)


# 定义梯度下降法：
def graDes(defaultTheta, X, Y, alpha, h):
    '''defaultTheta is a col vector,X is feature
    martix(one row is one attruibute),Y is target
    (a col vector),alpha is study rate,h is
    hopotheis function'''
    sum = np.zeros(defaultTheta.shape).T
    for i in range(Y.size):
        temp = (h(X[i].T, defaultTheta) - Y[i]) * X[i]  # get a row vector
        sum += temp
    defaultTheta = defaultTheta - (alpha * (1 / Y.size) * sum.T)
    return defaultTheta


# 绘制迭代图像


def drawIter(X, Y, theta, h, alpha, count):
    '''X is feature martix(onw row is one record),Y is target(a col
    vector),theta is a col vector'''
    figIter, axIter = plt.subplots()
    figIter.set_tight_layout(True)

    listY = []
    listY.append(costJ(X, Y, theta, h))
    for i in range(count):
        theta = graDes(theta, X, Y, alpha, h)
        listY.append(costJ(X, Y, theta, h))
    listX = np.arange(count + 1)
    axIter.scatter(listX, listY)
    plt.xlabel('#iters')
    plt.ylabel('''J's value''')
    axIter.set_title('J ~ #num ')

    plt.show()


# client code
dt = np.array([[65.0652905, 1.5233249, -18.09139454]]).T
res = np.array([res]).T
drawIter(dataX, Y, res, hy, 0.003, 100)
