'''
Created on April, 23, 2017

@author: Darcy
Topic: redge regression
Redge regression is used to decrease the number of paremeters as well as make X.T * X not singular
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

def redgeRegres(xArr, yArr, lam = 0.2):
	xMat = mat(xArr); yMat = mat(yArr).T 
	xTx = xMat.T * xMat
	m = shape(xMat)[1]
	diag = mat(eye(m)) * lam 
	denom = xTx + diag
	if linalg.det(denom) == 0:
		print "The matrix is singular"
		return
	w = denom.I * (xMat.T * yMat)
	return w 

def redgeTest(xArr, yArr):
	xMat = mat(xArr); yMat = mat(yArr).T 
	yMean = mean(yMat, 0)
	yMat = yMat - yMean
	xMeans = mean(xMat, 0)
	xVar = var(xMat, 0)
	xMat = (xMat - xMeans) / xVar
	numIte = 30
	wsMat = zeros((numIte, shape(xMat)[1]))
	for i in range(numIte):
		ws = redgeRegres(xArr, yArr, exp(i - 10))
		wsMat[i, :] = ws.T 
	return wsMat

def plot(xArr, yArr):
	weights = redgeTest(xArr, yArr)
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(weights)
	plt.show()


if __name__ == "__main__":
	x, y = loadDataSet('./data/abalone.txt')
	plot(x, y)
	



