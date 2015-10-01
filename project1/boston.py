import sklearn.datasets
import sklearn.linear_model as linear_model
import numpy.random
import numpy as np
import numpy.linalg
import matplotlib.pyplot as plt
from sklearn import ensemble
from sklearn.metrics import mean_squared_error
from sklearn.cross_validation import train_test_split
if __name__=="__main__":
    boston=sklearn.datasets.load_boston()
#Get the trainning data and test data
    rng=np.random.RandomState(13)
    trainFeatures,testFeatures,trainTarget,testTarget=train_test_split(boston.data,boston.target,test_size=len(boston.target)/3,random_state=rng)
#Create Reg
    RG=[
            ("LR",linear_model.LinearRegression()),
            ("RidgeR",linear_model.RidgeCV()),
            ("Lasso",linear_model.LassoCV(alphas=[0.01,0.05,0.1,0.5,1.0,10.0])),
            ("Elastic Net",linear_model.ElasticNetCV()),
    ]
#Draw
    X=range(len(testTarget))
    for name,rg in RG:
        w=open(name+"data",'w')
        w.write("testDta trueData\n")
        rg.fit(trainFeatures,trainTarget)
        y_pred=rg.predict(testFeatures)
        for i in range(len(y_pred)):
            w.write(str(y_pred[i])+" "+str(testTarget[i])+"\n")
        print name+"(Boston)Error:"+str(mean_squared_error(testTarget,y_pred))
        plt.plot(range(len(testTarget)),y_pred,'r--',label='Predict Price')
        plt.plot(X,testTarget,'g',label='True Price')
        legend=plt.legend()
        plt.title(name+" (Boston)")
        plt.ylabel("Price(1000 USD)")
        plt.savefig(name,format='png')
