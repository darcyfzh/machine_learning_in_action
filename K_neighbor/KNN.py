'''
@Author: Darcy
@Date: April, 23, 2017
Topic: K-neighbor
'''
#-*- encoding:utf-8 -*-
from numpy import *
import matplotlib.pyplot as plt

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    numFeat = len(open(fileName).readline().split('\t')) - 1 #get number of fields 
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(int(curLine[-1]))
    return dataMat,labelMat

def classify(inX, dataArr, labels, k):
	# inX and dataArr are both array-type, not matrix type
	# Otherwise there'll be wrong
    dataSetSize = dataArr.shape[0]
    diffArr = inX - dataArr
    sqDiffMat = square(diffArr)
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqrt(sqDistances)
    sortedDistIndicies = distances.argsort()     
    classCount = {}          
    for i in range(k):
        label = labels[sortedDistIndicies[i]]
        if label in classCount:
            classCount[label] += 1
        else:
            classCount[label] = 1
    #Notice that the item[1], not item[0], which means reverse key and value after been sorted
	sortedClassCount = sorted(classCount.iteritems(), key = lambda item:item[1], reverse=True)
	return int(sortedClassCount[0][0])

def autoNorm(dataSet):
	#min(dataSet, 0) is wrong , mean(dataSet, 0) and var(dataSet, 0) is right
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    #you can also use normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = dataSet - minVals
    normDataSet = normDataSet / ranges   #element wise divide
    return normDataSet, ranges, minVals
   
def ClassTest(dataArr, lebels, testRatio = 0.1):
    normMat, ranges, minVals = autoNorm(dataArr)
    m = normMat.shape[0]
    numTestVecs = int(m * testRatio)
    errorCount = 0.0
    result = []
    for i in range(numTestVecs):
        classifierResult = classify(normMat[i,:], normMat[numTestVecs:m,:], labels[numTestVecs:m], 3)
        print "the classifier came back with: {result}, the real answer is: {real}".format(result = classifierResult, real = labels[i])
        result.append([int(classifierResult), int(labels[i])])
        if (classifierResult != labels[i]): errorCount += 1.0
    #print "the total error rate is: %f" % (errorCount / float(numTestVecs))
    #print errorCount
    result = array(result)
    savetxt('./data/result.txt', result)


if __name__ =="__main__":
    data, labels = loadDataSet('./data/datingTestSet2.txt')
    dataArr = array(data)
    ClassTest(dataArr, labels, 0.2)




