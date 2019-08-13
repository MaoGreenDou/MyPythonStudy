# -*- coding: utf-8 -*-
__author__ = 'MaoDou'
__date__ = '2019/8/12 10:38'

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

sns.set_style('whitegrid')

# logistic hypothesis


def lhy(theta, x):
    '''theta(parameter vector) and x(feature vector)
     both are col vector'''
    temp = np.dot(theta.T, x)
    temp2 = 1 + np.exp(-temp)
    return float(1 / temp2)    # make sure return is a digit

# logistic cost function


def lcostJ(X, Y, theta, lhy):
    '''X is the feature ndarray(one row is one record)
    Y is the target vector(a col vector),theta is like
    lhy's, lhy is hypothesis'''
    sum = 0
    for i in range(Y.size):
        y = float(Y[i])
        h = lhy(theta, X[i])
        sum += y * np.log(h) + (1 - y) * np.log(1 - h)
    return -sum / Y.size

# logistic gradient descent algorithm


def lgraDes(X, Y, theta, alpha, lhy):
    '''X is the feature ndarray(one row is one record)
Y is the target vector(a col vector),theta is like
lhy's, lhy is hypothesis'''
    sum = np.zeros(theta.shape).T
    for i in range(Y.size):
        temp = (lhy(X[i].T, theta) - Y[i]) * X[i]  # get a row vector
        sum += temp
    theta = theta - (alpha * (1 / Y.size) * sum.T)
    return theta


# draw J and #iter 's scatter
def drawIter(X, Y, theta, h, alpha, count):
    '''X is feature martix(onw row is one record),Y is target(a col
    vector),theta is a col vector'''
    figIter, axIter = plt.subplots()
    figIter.set_tight_layout(True)
    res = theta
    listY = []
    listY.append(lcostJ(X, Y, theta, h))
    for i in range(count):
        theta = lgraDes(X, Y, theta, alpha, h)
        listY.append(lcostJ(X, Y, theta, h))
        if i == count - 1:
            res = theta
    listX = np.arange(count + 1)
    axIter.scatter(listX, listY)
    plt.xlabel('#iters')
    plt.ylabel('''J's value''')
    axIter.set_title('J ~ #num ')

    plt.show()
    return res

## logistic gradient descent with regularization
def lgraDes(X, Y, theta, alpha, lhy, lam = 0):
    '''X is the feature ndarray(one row is one record)
    Y is the target vector(a col vector),theta is like
    lhy's, lhy is hypothesis, lam is punishment
    parameter'''
    tempTheta = theta    # 保证theta是同时更新
    for i in range(len(theta)):
        sum = 0
        for j in range(len(Y)):
            temp = float( (lhy(X[j].T, theta) - Y[j]) * X[j,i] )
            sum += temp
        if i!=0:
            tempTheta[i] = theta[i]*(1-alpha*lam/len(Y)) - alpha*1/len(Y)*sum
        else:
            tempTheta[i] = theta[i] - alpha * 1 / len(Y) * sum    # 不对theta[0]进行惩罚
    return tempTheta




# client code
# neX1 = X[0:50,0]
# neX2 = X[0:50,1]
# poX1 = X[-51:-1,0]
# poX2 = X[-51:-1,1]
# plt.scatter(neX1,neX2,color='y',label='negative samples')
# plt.scatter(poX1,poX2,color='green',label='positive samples')
# plt.legend(loc='best')
# theta = np.zeros([3,1])
# neX1.shape
# poX1.shape
# temp1 = np.hstack((neX1.reshape(-1,1),neX2.reshape(-1,1)))
# temp1.shape
# temp2 = np.hstack((poX1.reshape(-1,1),poX2.reshape(-1,1)))
# temp2.shape
# temp = np.vstack((temp1,temp2))
# temp.shape
# dataX = np.hstack((np.ones([100,1]),temp))
# Y = np.zeros([50,1])
# Y = np.vstack((Y,np.ones(50,1)))
# Y = np.vstack((Y, np.ones([50, 1])))
# Y.shape
# Y
# dataX.shape
# dataY = Y
#
# res = drawIter(dataX,dataY,res,lhy,0.003,500000)
#
# plt.scatter(neX1,neX2,color='y',label='negative samples')
# plt.scatter(poX1,poX2,color='green',label='positive samples')
# plt.legend(loc='best')
# x = np.arange(10,30,0.1)
# y = -(float(res[1])/float(res[2]))*x - (float(res[0])/float(res[2]))
# plt.plot(x,y)
