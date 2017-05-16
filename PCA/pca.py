'''
@Author: Darcy
@Date: May, 16, 2017
@Topic: Primary component analysis
'''
import numpy as np
import matplotlib.pyplot as plt
def loadData(filName, delim = '\t'):
	fr = open(filName)
	stringArr = [line.strip().split(delim) for line in fr.readlines()]
	dataArr = [map(float, line) for line in stringArr]
	return np.mat(dataArr)

def pca(dataMat, topNfeat = 10000):
	meanVals = np.mean(dataMat, axis = 0)
	meanRemove = dataMat - meanVals
	covMat = np.cov(meanRemove, rowvar = 0)
	eigVals, eigenVecs = np.linalg.eig(covMat)
	eigValInd = np.argsort(-eigVals) # descending sort
	eigValIndNew = eigValInd[0:(topNfeat):1]
	eigenVecsNew = eigenVecs[:, eigValIndNew]
	newData = meanRemove * eigenVecsNew
	reNewData = newData * eigenVecsNew.T + meanVals
	return newData, reNewData

def comparePlot(origData, reNewData):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(origData[:, 0].flatten().A[0], origData[:, 1].flatten().A[0], marker = 'o', s = 50, c = 'red')
	ax.scatter(reNewData[:, 0].flatten().A[0], reNewData[:, 1].flatten().A[0], marker = '^', s = 90)
	plt.show()


'''
Decreaing dimension for semiconductor data
'''

#Replace NaN with mean value
def replaceNanWithMean(fileName):
	data = loadData(fileName, ' ')
	dataMat = np.mat(data)
	numFeat = np.shape(dataMat)[1]
	for i in range(numFeat):
		meanVal = np.mean(dataMat[np.nonzero(~np.isnan(dataMat[:, i]))[0], i])
		dataMat[np.nonzero(np.isnan(dataMat[:, i]))[0], i] = meanVal
	return dataMat

if __name__ == "__main__":
	dataMat_1 = loadData('./data/testSet.txt') 
	newData_1, reNewData_1 = pca(dataMat_1, 1)
	#comparePlot(dataMat_1, reNewData_1)
	dataMat_2 = replaceNanWithMean('./data/secom.data')
	


