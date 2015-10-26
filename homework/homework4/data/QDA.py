import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors
from sklearn.qda import QDA
def InitData(fn1,fn2,fn3,fn4):
    testData=open(fn1,'r')
    trainData=open(fn2,'r')
    testt=open(fn3,'r')
    traint=open(fn4,'r')
    test  = []
    testTarget=[]
    train = []
    trainTarget = []
    for line in testt:
        testTarget.append(line.strip())
    for line in traint:
        trainTarget.append(line.strip())
    for line in testData:
        line = line.split(',')
        if line[0]=='x.1':
            continue
        temp=[]
        for i in range(0,len(line)):
            if i<0:
                testTarget.append(float(line[i].strip()))
            else:
                temp.append(float(line[i].strip()))
        test.append(temp)
    for line in trainData:
        temp=[]
        line = line.split(',')
        if line[0]=='x.1':
            continue
        for i in range(0,len(line)):
            if i<0:
                trainTarget.append(float(line[i].strip()))
            else:
                temp.append(float(line[i].strip()))
        train.append(temp)
    return train,test,trainTarget,testTarget
if __name__ =='__main__':
    fn1='./test.data'
    fn2='./train.data'
    fn3='./testTarget.data'
    fn4='./trainTarget.data'
    train,test,trainTarget,testTarget=InitData(fn1,fn2,fn3,fn4)
    clf = QDA()
    clf.fit(train,trainTarget)
    y_pred=clf.predict(test)
    print "error"
    print 1-np.mean(y_pred==testTarget)






