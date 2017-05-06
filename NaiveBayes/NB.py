from numpy import *
def loadDataSet():
	postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
				 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
				 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
				 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
				 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
				 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
	classVec = [0,1,0,1,0,1]	#1 is abusive, 0 not
	return postingList,classVec

def createVocabList(dataSet):
	vocabSet = set([])
	for document in dataSet:
		vocabSet = vocabSet | set(document)
	return list(vocabSet)

def setOfWordToVec(vocabSet, inputSet):
	vec = [0] * len(vocabSet)
	for word in inputSet:
		if word in vocabSet:
			vec[vocabSet.index(word)] = 1
		else:
			print "the word:{} not in vocabulary".format(word)
	return vec

def trainNB(trainMatrix, trainLabels):
	m = len(trainMatrix)
	n = len(trainMatrix[0])
	pAbusive = sum(trainLabels) / m
	#p0Num = zeros(n); p1Num = zeros(n)
	p0Num = ones(n); p1Num = ones(n)
	p0Denom = 0.0; p1Denom = 0.0
	for i in range(m):
		if trainLabels[i] == 0:
			p0Num += trainMatrix[i]
			p0Denom += sum(trainMatrix[i])
		else:
			p1Num += trainMatrix[i]
			p1Denom += sum(trainMatrix[i])
	# p0Vect = p0Num / p0Denom
	# p1Vect = p1Num / p1Denom
	p0Vect = log(p0Num / p0Denom)
	p1Vect = log(p1Num / p1Denom)
	return p0Vect, p1Vect, pAbusive

def classifyNB(vect2Classify, p0Vect, p1Vect, pClass1):
	p1 = sum(p1Vect * vect2Classify) + log(pClass1)
	p0 = sum(p0Vect * vect2Classify) + log(1 - pClass1)
	if p0 > p1:
		return 0
	else:
		return 1

def bagOfWords2VecMN(vocabList, inputSet):
	returnVec = [0]*len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] += 1
	return returnVec

def textParse(bigString):	#input is big string, #output is word list
	import re
	listOfTokens = re.split(r'\W*', bigString)
	return [tok.lower() for tok in listOfTokens if len(tok) > 2] 

# def spamTest():
# 	docList=[]; classList = []; fullText =[]
# 	for i in range(1,26):
# 		wordList = textParse(open('email/spam/%d.txt' % i).read())
# 		docList.append(wordList)
# 		fullText.extend(wordList)
# 		classList.append(1)
# 		wordList = textParse(open('email/ham/%d.txt' % i).read())
# 		docList.append(wordList)
# 		fullText.extend(wordList)
# 		classList.append(0)
# 	vocabList = createVocabList(docList)#create vocabulary
# 	sumError = 0.0
# 	cvIters = 10
# 	for iter in range(cvIters):
# 		trainingSet = range(50); testSet=[]
# 		for i in range(10):
# 			randIndex = int(random.uniform(0,len(trainingSet)))
# 			testSet.append(trainingSet[randIndex])
# 			del(trainingSet[randIndex])  
# 		trainMat=[]; trainClasses = []
# 		for docIndex in trainingSet:#train the classifier (get probs) trainNB0
# 			trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
# 			trainClasses.append(classList[docIndex])
# 		p0V,p1V,pSpam = trainNB(array(trainMat),array(trainClasses))
# 		errorCount = 0
# 		for docIndex in testSet:		#classify the remaining items
# 			wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
# 			if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
# 				errorCount += 1
# 				#print "classification error",docList[docIndex]
# 		#return 'the error rate is: ',float(errorCount)/len(testSet)
# 		errorRate = float(errorCount) / len(testSet)
# 		sumError += errorRate
# 	meanError = sumError / cvIters
# 	return meanError

def spamTest():
    docList=[]; classList = []; fullText =[]
    for i in range(1,26):
        wordList = textParse(open('./data/email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('.data/email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)#create vocabulary
    trainingSet = range(50); testSet=[]           #create test set
    for i in range(10):
        randIndex = int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])  
    trainMat=[]; trainClasses = []
    for docIndex in trainingSet:#train the classifier (get probs) trainNB0
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB(array(trainMat),array(trainClasses))
    errorCount = 0
    for docIndex in testSet:        #classify the remaining items
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
            print "classification error",docList[docIndex]
    print 'the error rate is: ',float(errorCount)/len(testSet)


if __name__ == "__main__":
	# postingList,classVec = loadDataSet()
	# vocabSet = createVocabList(postingList)
	print spamTest()