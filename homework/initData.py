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
