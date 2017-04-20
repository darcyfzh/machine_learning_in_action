#K-neighbor 
#KNN没有显式的学习过程
#决策准则是经验风险最小化
#多数表决规则等价于经验风险最小化
from numpy import *
import operator
def classify(inx, dataSet, labels, k):
	dataSize = dataSet.shape[0]
	diffMat = tile(inx, (dataSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistance = sqDiffMat.sum(axis = 1)
	distance = sqDistance ** 0.5
	sortedDisIndex = distance.argsort() ## 从小到大排序后的索引值
	dic = {}
	for i in range(k):
	    label = label[sortedDisIndex[i]]
	    dic[label] += 1
	sortedDic = sorted(dic.items(), key = lambda item:item[1], reverse = True)
    return sortedDic[0][0]

