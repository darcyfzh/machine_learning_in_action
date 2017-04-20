from numpy import *
## 最小二乘法 w = inv(X.T * x) * X.T * y
def loadDataSet(file):
	dataMat = [];labelMat = []
	fr = open(file)
	for line in fr.readlines():
		lineArr = line.strip().split('\t')
		dataMat.append(lineArr[:-1])
		labelMat.append(lineArr[-1])
	return dataMat,labelMat

def standRegres(xArr,yArr):
	xMat = mat(xArr); yMat = mat(yArr).T 
	xTx = xMat.T * xMat
	if linalg.det(xTx) == 0:
		print "This matrix is singular"
		return
	ws = xTx.T * (xMat.T * yMat)
	return ws




