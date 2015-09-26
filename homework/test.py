from initData import InitData
import sklearn
from string import atof
from matplotlib import pyplot as plt
from sklearn import neighbors
from sklearn import linear_model
import numpy as np
import sys
def LR(test,clf):
    p=clf.predict(test)
    if abs(p-2)>=abs(p-3):
        return 3.0
    else:
        return 2.0
def getErr(trainData,trainTarget,testData,testTarget):
    clf=linear_model.LinearRegression()
    clf.fit(trainData,trainTarget)
    num=len(testTarget)
    erro=0;
    for i in range(num):
        if testTarget[i]!= LR(testData[i],clf):
            erro=erro+1
        else:
            continue
    print float(erro)/num
def getErr1(trainData,trainTarget,testData,testTarget,k):
    clf=neighbors.KNeighborsClassifier(k)
    clf.fit(trainData,trainTarget)
    num=len(testTarget)
    erro=0;
    for i in range(num):
        if testTarget[i]!= clf.predict(testData[i]):
            erro=erro+1
        else:
            continue
    print float(erro)/num
if __name__=='__main__':
    fn=sys.argv[1]
    trainData,trainTarget,testData,testTarget=InitData(fn)
    getErr(trainData,trainTarget,testData,testTarget)
    getErr1(trainData,trainTarget,testData,testTarget,15)
