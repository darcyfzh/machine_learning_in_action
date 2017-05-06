'''
@Author: Darcy 
@Date: May, 6, April
@Topic: Logistic Regression
'''
from numpy import *

def loadDataSet(fileName):
	data = []; label = []
	numFeats = len(open(fileName).readline().split('\t')) - 1
	fr = open(fileName)
	for line in fr.readlines():
		lineArr = []
		lineArr.append(1)
		currenLine = line.strip().split('\t')
		for i in range(numFeats):
			lineArr.append(float(currenLine[i]))
		data.append(lineArr)
		label.append(int(currenLine[-1]))
	return data, label

def sigmoid(inX):
    return 1.0 / (1+exp(-inX))

def gradDescent(data, labels):
    dataMat = mat(data)             #convert to NumPy matrix
    labelMat = mat(labels).T #convert to NumPy matrix
    m,n = shape(dataMat)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n,1))
    for k in range(maxCycles):              #heavy on matrix operations
        h = sigmoid(dataMat * weights)     #matrix mult
        error = h - labelMat               #vector subtraction
        weights = weights - alpha * dataMat.T * error #matrix mult
    return weights.T

def stocGradDescent0(data, labels):
    dataMat = array(data)
    m, n = shape(dataMat)
    alpha = 0.01
    weights = ones(n)   #initialize to all ones
    for i in range(m):
        h = sigmoid(sum(dataMat[i] * weights))
        error = h - labels[i]
        weights = weights - alpha * error * dataMat[i]
    return weights

def stocGradDescent1(data, labels, maxIter = 150):
	dataMat = array(data)
	m,n = shape(dataMat)
	weight = ones(n)
	for i in range(maxIter):
		dataIndex = range(m)
		for j in range(m):
			randomIndex = int(random.uniform(0, len(dataIndex)))
			alpha = 4/(1.0 + j + i) + 0.0001
			h = sigmoid(sum(dataMat[randomIndex] * weights))
            error = h - labels[randomIndex]
            weights = weights - alpha * error * dataMat[randomIndex]
            del(dataIndex(randomIndex))
	return weight

if __name__ == "__main__":
	data, label = loadDataSet('./data/testSet.txt')
	print stocGradAscent0(data, label)








