'''
Created on April, 23, 2017

@author: Darcy
Topic: linear regression
'''
#-*- encoding:utf-8 -*-
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

def standRegres(xArr, yArr):
	xMat = mat(xArr); yMat = mat(yArr).T 
	xTx = xMat.T * xMat
	if linalg.det(xTx) == 0.0:
		print " the matrix is singular"
		return 
	w = xTx.I * (xMat.T * yMat)
	return w

def plot(xArr, yArr, w):
	xMat = mat(xArr); yMat = mat(yArr)
	yNew = xMat * w
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(xMat[:, 1].flatten().A[0], yMat.T[:,0].flatten().A[0])
	xCopy = xMat.copy() # difference between cpoy and deepcopy
	xCopy.sort(0)
	yNew = xCopy * w 
	ax.plot(xCopy[:, 1], yNew)
	plt.show()

# correlation between true value and predicted value
def correlation(xArr, yArr, w):
	xMat = mat(xArr)
	yMat = mat(yArr)
	yNew = xMat * w
	cor = corrcoef(yNew.T, yMat)
	return cor
	
if __name__ == "__main__":
	x, y = loadDataSet('./data/ex0.txt')
	weight = standRegres(x, y)
	cor = correlation(x, y, weight)
	print cor
	plot(x, y, weight)







