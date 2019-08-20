#-*- coding: utf-8 -*-
__author__ = 'MaoDou'
__date__ = '2019/8/17 17:30'

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

''' 

    这份文档包括如下神经网络代码实现的全过程：
    1.激活函数
    2.前向传播计算输出
    3.计算代价函数
    4.计算偏导数
    5.梯度下降算法的应用  
    6.绘制代价函数和迭代次数图像
    7.偏导数的验证
    8.预测函数
    9.用户端代码（包含决策边界的绘制）
    测试使用的数据集来自‘sklearn的breast_cancer’
    
'''

def sigmoid(x):
    ''' sigmoid（）激活函数。

    x can be a digit or a vector。

    返回值可以是标量或矢量'''

    return 1/(1 + np.exp(-x))

def nHy(x, theta_1, theta_2):
    '''nHy（）输出函数。

    x is feature vector(a col vector),
    theta_1 and theta_2 are parameter ma-
    -rtixs。

    该输出函数定义了一个神经网络结构，该神经
    网络结构：
    三层：输入（2+1b）-隐藏（3+1b）-输出（1）

    返回值是一个元组：
    （浮点型输出，第一层激活值，第二层激活值，第三
    层激活值，第二层中间值，第三层中间值）
    '''

    # assure the structure of the net.
    # define the activity items
    a_1 = np.zeros([3, 1])
    a_2 = np.zeros([3, 1])
    a_3 = np.zeros([1, 1])
    # define the temp
    z_2 = np.zeros([3, 1])
    z_3 = np.zeros([1, 1])
    # initial the activity one
    a_1 = x
    z_2 = np.dot(theta_1,a_1)    # return a col vector 3*1
    a_2 = sigmoid(z_2)
    a_2 = np.vstack( ( np.ones([1,1]),a_2 ) )
    z_3 = np.dot(theta_2,a_2)    # return a col vector 1*1
    a_3 = sigmoid(z_3)
    return ( float(a_3),a_1,a_2,a_3,z_2,z_3 )

def ncostJ(X, Y, theta_1,theta_2,lam=0):
    '''ncostJ（）代价函数

    X is the feature ndarray(one row is one record)
    Y is the target vector(a col vector),theta_1 and
    theta_2 are parameter martixs.

    该函数定义了二分类神经网络的代价函数，sum项定义了-L函数，re
    为正则项，默认为零

    返回值是浮点型的代价函数'''


    sum = 0
    for i in range(Y.size):
        y = float(Y[i])
        h = nHy(X[i].reshape(-1,1),theta_1,theta_2)
        sum += y * np.log(h[0]) + (1 - y) * np.log(1 - h[0])
    # wait to regularization
    reTheta = np.vstack((theta_1.reshape(-1,1),theta_2.reshape(-1,1)))
    re = 0
    for i in range(reTheta.size):
        re += float(np.power(reTheta[i], 2))
    return -sum / Y.size + (lam/(2*Y.size))*re



def calPd(X,Y,theta_1,theta_2,lam=0):
    '''calPd()函数

    X is the feature ndarray(one row is one record)
    Y is the target vector(a col vector),theta_1 and
    theta_2 are parameter martixs.

    该函数利用反向传播算法计算权重矩阵的偏导数

    返回值是一个元组：
    （权重矩阵一的偏导矩阵，权重矩阵二的偏导矩阵），
    可选择是否包含正则项'''

    delta_1 = np.zeros(theta_1.shape)
    delta_2 = np.zeros(theta_2.shape)

    for i in range(Y.size):
        res = nHy(X[i].reshape(-1,1),theta_1,theta_2)
        err_3 = res[0] - Y[i]
        err_3 = err_3.reshape(1,1)    # a 1*1 col vector
        err_2 = np.dot(theta_2.T,err_3)*( res[2]*(1-res[2]) )    # a 4*1 col vector

        delta_2 += np.dot(err_3,res[2].T)
        delta_1 += np.dot(err_2[1:],res[1].T)

    de_2 = (1/Y.size)*delta_2    # a 1*4 martix
    de_1 = (1/Y.size)*delta_1    # a 3*3 martix

    return (de_1,de_2)


def ngradDes(X,Y,theta_1,theta_2,alpha,lam=0):
    '''ngradDes()函数

    X is the feature ndarray(one row is one record)
   Y is the target vector(a col vector),theta_1 and
   theta_2 are feature martixs, alpha is study rating,
   lam is punishment parameter.

    该函数定义了梯度下降算法在神经网络中的应用，包含
    正则化处理（不包括偏置项）

    返回值是一个元组：
    （更新后的权重矩阵一，更新后的权重矩阵二）'''

    der = calPd(X,Y,theta_1,theta_2,lam)

    temp_1 = theta_1*(1 - alpha*lam/Y.size) - alpha*der[0]
    theta_1 = theta_1 - alpha*der[0]
    theta_1[:,1:] = temp_1[:,1:]

    temp_2 = theta_2*(1 - alpha * lam / Y.size) - alpha * der[1]
    theta_2 = theta_2 - alpha*der[1]
    theta_2[:, 1:] = temp_2[:,1:]

    return (theta_1,theta_2)


def drawIter(X, Y, theta_1,theta_2, alpha, count,lam=0):
    '''drawIter()函数

    X is feature martix(onw row is one record),Y is target(a col
    vector),theta is a col vector

    该函数将绘制代价值和迭代次数的图像，代价值尚未实现正则化

    返回值是一个元组：
    （最后一次迭代得到的权重矩阵一，最后一次迭代得到的权重矩阵二）'''


    figIter, axIter = plt.subplots()
    figIter.set_tight_layout(True)
    res = (theta_1,theta_2)
    listY = []
    listY.append(ncostJ(X, Y, theta_1,theta_2,lam))
    for i in range(count):
        (theta_1,theta_2) = ngradDes(X, Y, theta_1,theta_2, alpha, lam)
        listY.append(ncostJ(X, Y, theta_1,theta_2, lam))
        if i == count - 1:
            res = (theta_1,theta_2)
    listX = np.arange(count + 1)
    axIter.scatter(listX, listY)
    plt.xlabel('#iters')
    plt.ylabel('''J's value''')
    axIter.set_title('J ~ #num ')

    plt.show()
    return res

def vD(X,Y,theta_1,theta_2,lam=0):
    '''
    vD()函数

    :param X:特征矩阵（数据集），每一行是一条记录
    :param Y:目标向量，是一个列向量
    :param theta_1: 权重矩阵一
    :param theta_2: 权重矩阵二
    :param lam: 惩罚参数

    该函数通过割线斜率近似得到两个偏导数矩阵

    :return: 返回一个元组：
    （近似得到的偏导数矩阵一，近似得到的偏导数矩阵二）
    '''

    EPS = 10e-4
    theta = np.vstack((theta_1.reshape(-1,1),theta_2.reshape(-1,1)))    # 9*1(from 3*3) + 4*1(from 1*4) = 13*1 col vector
    vD = np.zeros(theta.shape)    # serve verify derivative
    for i in range(len(theta)):
        thetaPlus = theta.copy()    # 注意python的内存机制
        thetaPlus[i] = thetaPlus[i] + EPS
        thetaMinus = theta.copy()
        thetaMinus[i] = thetaMinus[i] - EPS

        temp1 = thetaPlus[0:9].reshape(3,3)
        temp2 = thetaPlus[9:].reshape(1,4)

        temp3 = thetaMinus[0:9].reshape(3,3)
        temp4 = thetaMinus[9:].reshape(1,4)

        vD[i] = (ncostJ(X,Y,temp1,temp2,lam)-ncostJ(X,Y,temp3,temp4,lam))/(2*EPS)

    vD_1 = vD[0:9].reshape(3,3)
    vD_2 = vD[9:].reshape(1,4)

    return (vD_1,vD_2)




def predict(X,theta_1,theta_2):

    '''
    predict()函数

    :param X: 特征矩阵（数据集），每一行是一条记录
    :param theta_1:权重矩阵一
    :param theta_2:权重矩阵二

    预测函数预测输入权重矩阵下的每个数据的标签

    :return:返回值是一个数组，元素是每个数据的标签

    '''

    listY = []
    for i in range(X.shape[0]):
        listY.append(nHy(X[i].reshape(-1,1),theta_1,theta_2)[0])

    res = np.array(listY)
    for i in range(len(listY)):
        if listY[i]>=0.5:
            res[i] = 1
        else:
            res[i] = 0
    return res

#c客户端代码
cancer = datasets.load_breast_cancer()
X = cancer.data
Y = cancer.target[0:100].reshape(-1,1)
dataX = np.hstack((X[0:100,0].reshape(-1,1),X[0:100,1].reshape(-1,1)))
dataX = np.hstack((np.ones([100,1]),dataX))

theta_1 = np.random.rand(3,3)
theta_2 = np.random.rand(1,4)
calPd(dataX,Y,theta_1,theta_2)
vD(dataX,Y,theta_1,theta_2)




#绘制幕布
x_min, x_max = dataX[:,1].min() - .5 , dataX[:,1].max() + .5
y_min, y_max = dataX[:,2].min() - .5 , dataX[:,2].max() + .5
h = 0.01
xx, yy = np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))
#预测幕布上点的输出
pre = np.c_[xx.ravel(), yy.ravel()]
pre = np.c_[np.ones( [xx.ravel().size,1] ),pre]
Z = predict(pre,theta_1,theta_2)
Z = Z.reshape(xx.shape)
# 然后画出图
plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
plt.scatter(dataX[:, 1], dataX[:, 2], c=cancer.target[0:100], cmap=plt.cm.Spectral)

#
#
# (array([[ 0.50852998,  0.96852733,  0.10212747],
#         [ 0.03978172,  0.4850362 ,  0.46002113],
#         [-9.48317498,  0.45951809,  0.17473933]]),
#  array([[  1.86500051,   1.40756802,   1.38930858, -10.05485819]]))