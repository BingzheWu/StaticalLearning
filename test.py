import sklearn
from string import atof
from matplotlib import pyplot as plt
from sklearn import neighbors
from sklearn import linear_model
import numpy as np
import sys
reload(sys)
def InitData(fn):
    test=open(fn+'test','r')
    train=open(fn+'train','r')
    testData=[]
    trainData=[]
    trainTarget=[]
    testTarget=[]
    for line in train:
        line=line.split(' ');
        target=(atof(line[0].strip()))
        if target==2.0 or target==3.0: 
            trainTarget.append(target)
            image=[]
            for i in range(1,len(line)-1):
                image.append(atof(line[i].strip()));
            image=np.array(image)
            trainData.append(image)
        else:
            continue
    for line in test:
        line=line.split(' ');
        target=(atof(line[0].strip()))
        if target==2 or target==3:
            testTarget.append(target)
            image=[]
            for i in range(1,len(line)):
                image.append(atof(line[i].strip()));
            image=np.array(image)
            testData.append(image)
        else:
            continue
    return trainData,trainTarget,testData,testTarget
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
