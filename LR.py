##Logistic Regression
from numpy import *
import matplotlib.pyplot as plt
def loadData():
	dataSet = []
	labelSet = []
	f = open('input.txt')
    for line in f.realines():
    	value = line.strip().split()
    	dataSet.append(1.0,value[0],value[1])
    	labelSet.append(value[2])
    return dataSet, labelSet

def Sigmoid(a):
	return 1.0 / (1 + exp(-a))

##Gradient Ascent
def gradascent(data, label):
	dataMatrix = mat(data)
	labelMatrix = mat(label).transpose()
	m,n = shape(dataMatrix)
	weights = zeros((n,1))
	maxCycles = 500
	alpha = 0.01
	for i in range(maxCycles):
		h = Sigmoid(dataMatrix * weights) #(m*n) * (n*1)
		error = labelMatrix - h
		weights = weights + alpha * dataMatrix.transpose() * error   #(m*n).transpose * m*1
	return weights


def plotBestFit(weights):
	data,label = loadData()
	dataArr = array(data)
	n = shape(dataArr)[0]
	xcord1 = []
	ycord1 = []
	xcord2 = []
	ycord2 = []
	for i in range(n):
		if int(label[i]) == 1:
			xcord1.append(dataArr[i,1])
			ycord1.append(dataArr[i,2])
		else:
			xcord2.append(dataArr[i,1])
			ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s = 30,c = 'red',marker = 's')
    ax.scatter(xcord2,ycord2,s = 30,c = 'green')
    x = arange(-3.0,3.0,0.1)
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x,y)
    plt.show()


##Stochastic gradient descent
def SGD(data, label):
	dataMatrix = mat(data)
	labelMatrix = mat(label)
	alpha = 0.01
	m,n = shape(dataMatrix)
	weights = zeros((n,1))
	for i in range(m):
	    h = Sigmoid(sum(dataMatrix[i] * weights))
	    error = labelMatrix[i] - h
	    weights += alpha * error * dataMatrix[i]
	return weights	

##Mini-batch gradient descent
def MBGD(data, label,k):
	dataMatrix = mat(data)
	labelMatrix = mat(label)
	alpha = 0.01
	m,n = shape(dataMatrix)
	weights = zeros((n,1))
	for i in range(0,m,k):
		for j in range(i,k):
			h = Sigmoid(sum(dataMatrix[j] * weights))
	        error = labelMatrix[j] - h
	        weights += alpha * error * dataMatrix[j]
	return weights

