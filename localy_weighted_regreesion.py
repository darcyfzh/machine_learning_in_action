from numpy import *

def lwlr(testPoint,xArr,yArr,k = 1):
	xMat = mat(xArr);yMat = mat(yArr).T 
	m = shape(xMat)[0]
	weights = mat(eye(m))
	for i in range(m):
	    diff = testPoint - xArr[j,:]
	    weights[i,i] = exp(diff * diff.T / (-2 * k ** 2))
	xTx = xMat.T * (weights * xMat)
	if linalg.det(xTx) == 0.0:
	    print "the matrix is singular"
	ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint

def lwlrTest(testArr,xArr,yArr,k = 1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i],xArr,yArr,k = 1.0)
    return yMat 