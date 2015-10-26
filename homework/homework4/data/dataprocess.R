require(splines)
train=read.csv("train.data")
dim(train[2,])
for (i in 1:3040){
    temp=bs(train[i,],degree=10)
    temp=matrix(temp)
    dim(temp)=c(256,10)
    temp=t(temp)
    dim(temp)
    tmp=t(train[i,])
    xx=temp%*%tmp
    dim(xx)=c(1,10)
    print(xx[1,])
}
