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
def LR(testData,testTarget,trainData,trainTarget):
    clf=linear_model.LinearRegression()
    clf.
if __name__=='__main__':
    fn=sys.argv[1]
    trainData,trainTarget,testData,testTarget=InitData(fn)
    clf1=neighbors.KNeighborsClassifier(3)
    clf1.fit(trainData,trainTarget)
    clf2=linear_model.LinearRegression()
    clf2.fit(trainData,trainTarget)
    print(clf2.predict(testData[0]))
    print(clf1.predict(testData[0]))
    print(testTarget[2])




