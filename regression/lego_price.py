'''
@Author: Darcy
@Date: April, 23, 2017
@Topic: To bulid a price model of LEGO, find best lambda via cross validation
'''
#-*-encoding:uf-8-*-

from time import sleep
import json
import urllib2
def searchForSet(retX, retY, setNum, yr, numPce, origPrc):
    sleep(10)
    myAPIstr = 'AIzaSyD2cR2KFyx12hXu6PFU-wrWot3NXvko8vY'
    searchURL = 'https://www.googleapis.com/shopping/search/v1/public/products?key=%s&country=US&q=lego+%d&alt=json' % (myAPIstr, setNum)
    pg = urllib2.urlopen(searchURL)
    retDict = json.loads(pg.read())
    for i in range(len(retDict['items'])):
        try:
            currItem = retDict['items'][i]
            if currItem['product']['condition'] == 'new':
                newFlag = 1
            else: newFlag = 0
            listOfInv = currItem['product']['inventories']
            for item in listOfInv:
                sellingPrice = item['price']
                if  sellingPrice > origPrc * 0.5:
                    print "%d\t%d\t%d\t%f\t%f" % (yr,numPce,newFlag,origPrc, sellingPrice)
                    retX.append([yr, numPce, newFlag, origPrc])
                    retY.append(sellingPrice)
        except: print 'problem with item %d' % i
    
def setDataCollect(retX, retY):
    searchForSet(retX, retY, 8288, 2006, 800, 49.99)
    searchForSet(retX, retY, 10030, 2002, 3096, 269.99)
    searchForSet(retX, retY, 10179, 2007, 5195, 499.99)
    searchForSet(retX, retY, 10181, 2007, 3428, 199.99)
    searchForSet(retX, retY, 10189, 2008, 5922, 299.99)
    searchForSet(retX, retY, 10196, 2009, 3263, 249.99)

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
		ws = redgeRegres(xMat, yMat, exp(i - 10))
		wsMat[i, :] = ws.T 
	return wsMat

def error(yArr,yNew):
	return ((yArr - yNew) ** 2).sum()

def crossValidation(xArr, yArr, numVal):
	m = shape(xArr)[0]
	n = shape(xArr)[1]
	x = ones((m, n + 1))
	x[:, 1: 5] = xArr
	indexList = range(m)
	errorMat = zeros((numVal, 30))
	for i in range(numVal):
		trainX = []; trainY = [];
		testX = []; testY = []
		random.shuffle(indexList)
		for j in range(m):
			if j < 0.9 * m:
				trainX.append(xArr[indexList[j]])
				trainY.append(yArr[indexList[j]])
			else:
				testX.append(xArr[indexList[j]])
				testY.append(yArr[indexList[j]])
		wMat = redgeTest(trainX, trainY)
		for k in range(30):
			matTestX = mat(testX); matTrainX = mat(trainX)
			meanTrain = mean(matTrainX, 0)
			varTrain = var(matTrainX, 0)
			matTestX = (matTestX - meanTrain) / varTrain
			yEst = matTestX * wMat[k, :].T + mean(trainY)
			errorMat[i, k] = error(yEst.T, mat(testY))
	meanError = mean(errorMat, 0)
	minMean = float(min(meanError))
	bestWeight = wMat[nonzero(minMean == meanError)]
	return bestWeight

if __name__ == "__main__":
	x = []; y = []
	xArr, yArr = setDataCollect(x, y)
	bestWeight = crossValidation(xArr, yArr, 10)
	print bestWeight

