//K-means

from numpy import * 
def distEclud(vecA,vecB):
	return sqrt(sum((vecB - vecA) ** 2))

def randCent(dataSet,k):
	n = shape(dataSet)[1]
	centroids = zeros((k,n))
	for j in range(n):
		minJ = min(dataSet[:,j])
		rangeJ = float(max(dataSet[:j]) - minJ)
		centroids[:j] = minJ + rangeJ * random.randn(k,1)
	return centroids

def kMeans(dataSet,k,disMeas = distEclud,createCent = randCent):
    m = shape(dataSet)[0]
    n = shape(dataSet)[1]
	clusterAssment = zeros((m,2))
	centroids = createCent(dataSet,k)
	clusterChange = True	
	while clusterChange:
		clusterChange = False
		for i in range(m):
			minDist = inf
			minIndex = -1
			for j in range(k):
				distJ = disMeas(dataSet[i,:],centroids[j,:])
				if distJ < minDist:
					minDist = distJ;minIndex = j
			if clusterAssment[i,0] != minIndex:
				clusterChange = True
			clusterAssment[i,:] = minIndex, minDist ** 2
		dic = {}
		for i in range(m):
			dic[clusterAssment[i,0]].append(array(dataSet[i])
		for key in dic:
			sum = dic[key].sum(axis = 0)
			sum = sum / n
			centroids[k] = sum
	return centroids,clusterAssment
