import sklearn.datasets
import sklearn.linear_model
import numpy.random
import numpy as np
import numpy.linalg
import matplotlib.pyplot
from sklearn.cross_validation import train_test_split
if __name__=="__main__":
    boston=sklearn.datasets.load_boston()
#Get the trainning data and test data
    rng=np.random.RandomState(21)
    trainFeatures,testFeatures,trainTarget,testTarget=train_test_split(boston.data,boston.target,test_size=len(boston.target)/2,random_state=rng)
#Create Reg

#Train
    LR=sklearn.linear_model.LinearRegression()
    LR.fit(trainFeatures,trainTarget)
#Predict
    predictTargets=LR.predict(testFeatures)
#Evaluation
    print"Ordinary Least Squares(Boston)Error:"+str(1-np.mean(predictTargets==testTarget))
#Draw
    X=range(len(testTarget))
    matplotlib.pyplot.plot(range(len(testTarget)),predictTargets,'r--',label='Predict Price')
    matplotlib.pyplot.plot(X,testTarget,'g',label='True Price')
    legend=matplotlib.pyplot.legend()
    matplotlib.pyplot.show()
