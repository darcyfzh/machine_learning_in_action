'''
@Author : Darcy
@Date : April, 23, 2017
Topic : locally weighted regression
'''
from numpy import *
import pandas as pd
import matplotlib.pyplot as plt 

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    numFeat = len(open(fileName).readline().split('\t')) - 1 #get number of fields 
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat

def lwlr(testPoint, xArr, yArr, k = 1.0):
	xMat = mat(xArr)
	yMat = mat(yArr).T 
	m = shape(xMat)[0]
	weights = mat(eye(m))
	for i in range(m):
		diff = testPoint - xMat[i, :]
		weights[i, i] = exp(diff * diff.T / (-2.0 * k ** 2))
	xTx = xMat.T * (weights * xMat)
	if linalg.det(xTx) == 0:
		print "the matrix is singular"
		return 
	ws = xTx.I * (xMat.T * (weights * yMat))
	return testPoint * ws 

def lwlrTest(testArr, xArr, yArr, k = 1.0):
	m = shape(testArr)[0]
	yNew = zeros(m)
	for i in range(m):
		yNew[i] = lwlr(testArr[i], xArr, yArr, k)
	return yNew

def plot(xArr, yArr, yNew):
	xMat = mat(xArr)
	sortIndex = xMat[:, 1].argsort(0)
	xSort = xMat[sortIndex][:, 0, :]
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(xSort[:, 1], yNew[sortIndex])
	ax.scatter(xMat[:, 1].flatten().A[0], mat(yArr).T.flatten().A[0], s = 2, c = 'red')
	plt.show()

if __name__ == "__main__":
	x, y = loadDataSet('./data/ex0.txt')
	yNew = lwlrTest(x, x, y, 0.01)
	plot(x, y, yNew)