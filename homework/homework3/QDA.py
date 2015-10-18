import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors
from sklearn.qda import QDA
def InitData(fn1,fn2):
    testData=open(fn1,'r')
    trainData=open(fn2,'r')
    test  = []
    testTarget=[]
    train = []
    trainTarget = []
    for line in testData:
        line = line.split(',')
        if line[0]=='row.names':
            continue
        temp=[]
        for i in range(1,len(line)):
            if i==1:
                testTarget.append(float(line[i].strip()))
            else:
                temp.append(float(line[i].strip()))
        test.append(temp)
    for line in trainData:
        temp=[]
        line = line.split(',')
        if line[0]=='row.names':
            continue
        for i in range(1,len(line)):
            if i==1:
                trainTarget.append(float(line[i].strip()))
            else:
                temp.append(float(line[i].strip()))
        train.append(temp)
    return train,test,trainTarget,testTarget
if __name__ =='__main__':
    fn1='./data/vowel.test'
    fn2='./data/vowel.train'
    train,test,trainTarget,testTarget=InitData(fn1,fn2)
    clf = QDA()
    clf.fit(train,trainTarget)
    y_pred=clf.predict(test)
    print "error"
    print 1-np.mean(y_pred==testTarget)






