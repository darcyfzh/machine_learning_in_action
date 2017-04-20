#Naive bayes
#使用NB进行文本分类(0,1)
from numpy import *
#计算三个参数
def trainNB0(dataSet, labels):
	numTrainDoc = len(dataSet)
	numWords = len(dataSet[0])
	pClass1 = sum(labels) / float(numTrainDoc) #类别为1的概率
	p0Num = zeros(numWords)
	p1Num = zeros(numWords)
	p0Denom = 0
	p1Denom = 0
	for i in range(numTrainDoc):
		if labels[i] == 1:
			p1Num += dataSet[i]
            p1Denom += sum(dataSet[i])
        else:
            p0Num += dataSet[i]
            p0Denom += sum(dataSet[i])
    # p1Vect = p1Num / p1Denom 
    # p0Vect = p0Num / p0Denom
    #w为了使乘积转化为累加，此处取对数 
    p1Vect = log(p1Num / p1Denom) #文档类别为1时各单词出现的概率
    p0Vect = log(p0Num / p0Denom)
    return p0Vect, p1Vect, pClass1

def classifyNB(testVec, p0Vect, p1Vect, pClass1):
    p1 = sum(testVec * p1Vect) + log(pClass1)
    p0 = sum(testVec * p0Vect) + log(1 - pClass1)
    if p1 > p0:
    	return 1
    else:
    	return 0



