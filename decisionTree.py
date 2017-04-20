#Decision Tree
#计算香农熵
from numpy import *
from math import log
def calShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for vec in dataSet:
		currentLabel = vec[-1]
		if currentLabel not in labelCounts:
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1
	shannonEnt = 0.0
	for key in labelCounts:
		prob = labelCounts[key] / numEntries
		shannonEnt -= prob * log(prob, 2)
	return shannonEnt

#按照给定特征划分数据集
def splitDataSet(dataSet, axis, value): # 参数：数据集，划分数据集的特征，特征的值
	newData = []
	for vec in dataSet:
		if vec[axis] = value:
			newVec = vec[:axis]
			newVec.extend(vec[axis + 1:])
			newData.append(newVec)
	return newData


#选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
	numOfFeatures = len(dataSet[0]) - 1
	baseEntropy = calShannonEnt(dataSet)
	bestInfoGain = 0.0
	bestFeatures = -1
	for i in range(numOfFeatures):
		feaList = [example[i] for example in dataSet]
		uniqueVals = set(feaList)
		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet, i, value)
			prob = float(len(subDataSet) / len(dataSet))
			newEntropy += prob * calShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntropy
		if infoGain > bestInfoGain :
		    bestInfoGain = infoGain
		    bestFeature = i   
    return bestFeature

def majorityCnt(classList):
	classCount = {}
	for class in classList:
		if class not in classList:
			classCount[class] = 0
		classCount[class] += 1
	sortedClass = sorted(classCount, lambda item:item[1], reverse = True)
	return sortedClass[0][0]
#递归创建树
def createTree(dataSet, labels):
	classList = [example[-1] for example in dataSet]
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	if len(dataSet[0] == 1):
		return majorityCnt(classList)
	bestFeat = chooseBestFeatureToSplit(dataSet)
	bestFeatLabel = labels[bestFeature]
	myTree = {bestFeatLabel:{}}
	del labels[bestFeat]
	feaList = [example[bestFeat] for example in dataSet]
	uniqueVals = set(feaList)
	for value in uniqueVals:
		sublabels = labels[:]
		myTree[bestFeatLabel][value] = createTree(splitDataSet\
			                      (dataSet), bestFeat, value), sublabels)
    return myTree
