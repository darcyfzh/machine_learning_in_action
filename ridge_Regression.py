##Ridge regression
from numpy import *
def ridgeRegres(xMat,yMat,lam = 0.2):
	xTx = xMat.T * xMat
	denom = xTx + eye(shape(xMat)[1]) * lam
	if linalg.det(denom) == 0.0:
		print "This matrix is singular"
    yMat = yMat.T
	ws = denom.I * xMat.T * yMat
	return ws

def ridgeTest(xArr,yArr):
	xMat = mat(xArr)
	yMat = mat(yArr).T
	xMean = mean(xMat,0)
	xVar = var(xMat,0)
	yMean = mean(yMat,0)
	xMat = (xMat - xMean) / xVar
	yMat = yMat - yMean
	ws = ridgeTest(xMat,yMat,0.2)
	return ms





