import sklearn.datasets
import sklearn.linear_model
import numpy.random
import numpy as np
import numpy.linalg
from matplotlib import pyplot as plt
from sklearn import ensemble
from sklearn.metrics import mean_squared_error
from sklearn.cross_validation import train_test_split
if __name__=="__main__":
    boston=sklearn.datasets.load_boston()
#Get the trainning data and test data
    rng=np.random.RandomState(13)
    trainFeatures,testFeatures,trainTarget,testTarget=train_test_split(boston.data,boston.target,test_size=len(boston.target)/3,random_state=rng)
    trainFeatures[:,0]=np.log(trainFeatures[:,0])
    testFeatures[:,0]=np.log(testFeatures[:,0])
#set parameter
    params={'n_estimators': 500,'max_depth':4,'min_samples_split':1,'learning_rate':0.01,'loss':'ls'}
#train 
    rg=ensemble.GradientBoostingRegressor(**params)
#Plot feature importance 
    rg.fit(trainFeatures,trainTarget)
    y_pred=rg.predict(testFeatures)
    featureImportance=rg.feature_importances_
    X=range(len(testTarget))
    featureImportance=100.0*(featureImportance / featureImportance.max())
    sortedIdx=np.argsort(featureImportance)
    pos = np.arange(sortedIdx.shape[0])+.5
    plt.barh(pos,featureImportance[sortedIdx],align='center')
    plt.yticks(pos,boston.feature_names[sortedIdx])
    plt.xlabel('Relative Importance')
    plt.title('Variable Importance')
    plt.savefig("Importance",format='png')
    plt.show()
    #print Data
    print "GBR(Boston)Error:"+str(mean_squared_error(testTarget,y_pred))
    plt.plot(range(len(testTarget)),y_pred,label='Predict Price')
    print "test"+" true"
    for i in range(len(y_pred)):
        print str(y_pred[i])+" "+str(testTarget[i])
    plt.plot(X,testTarget,label='True Price')
    legend=plt.legend()
    plt.title("GBR"+" (Boston)")
    plt.ylabel("Price(1000 USD)")
    plt.savefig("GBR",format='png')
    plt.show()


    
