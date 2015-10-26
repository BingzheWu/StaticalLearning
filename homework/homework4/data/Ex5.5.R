#Author: 王莉晶 1300012406 
#Date: 2015.10.25
data = read.table("phoneme.data",header = T, sep = ",",fill = TRUE)
data1 = data[data$g=="aa",]
data2 = data[data$g=="ao",]
mydata = rbind(data1,data2)
#构造ten fold cross validation
require(caret)
flds <- createFolds(mydata$g, k = 10, list = TRUE, returnTrain = FALSE)



#用log回归求出beta
#1
r = multinom(formula = g~.-speaker-row.names, data = mydata[-flds[[1]],],MaxNWts=3000)
beta = summary(r)$coefficients
#H = bs(beta[2:257],df = 12)
#H = bs(beta[2:257],df = 12, knots=c(25,50,75,100,125,150,175,200,225,250))
#H = bs(beta[2:257],df = 24)
#H = bs(beta[2:257],df = 36)
H = bs(beta[2:257],df = 48)
x= t(H)%*%t(mydata[-flds[[1]],2:257])
x_star = t(x)
vect=as.vector(mydata[-flds[[1]],258])
z = qda(x_star,vect)
x_pred=t(H)%*%t(mydata[flds[[1]],2:257])
x_star_pred = t(x_pred)
vect_pred=as.vector(mydata[flds[[1]],258])
pred = predict(z,x_star_pred)$class
summary(pred == vect_pred)

#2
r = multinom(formula = g~.-speaker-row.names, data = mydata[-flds[[2]],],MaxNWts=3000)
beta = summary(r)$coefficients
#H = bs(beta[2:257],df = 12)
#H = bs(beta[2:257],df = 12, knots=c(25,50,75,100,125,150,175,200,225,250))
#H = bs(beta[2:257],df = 24)
H = bs(beta[2:257],df = 36)
#H = bs(beta[2:257],df = 48)
x= t(H)%*%t(mydata[-flds[[2]],2:257])
x_star = t(x)
vect=as.vector(mydata[-flds[[2]],258])
z = qda(x_star,vect)
x_pred=t(H)%*%t(mydata[flds[[2]],2:257])
x_star_pred = t(x_pred)
vect_pred=as.vector(mydata[flds[[2]],258])
pred = predict(z,x_star_pred)$class
summary(pred == vect_pred)

#3
r = multinom(formula = g~.-speaker-row.names, data = mydata[-flds[[3]],],MaxNWts=3000)
beta = summary(r)$coefficients
#H = bs(beta[2:257],df = 12)
#H = bs(beta[2:257],df = 12, knots=c(25,50,75,100,125,150,175,200,225,250))
#H = bs(beta[2:257],df = 24)
#H = bs(beta[2:257],df = 36)
H = bs(beta[2:257],df = 48)
x= t(H)%*%t(mydata[-flds[[3]],2:257])
x_star = t(x)
vect=as.vector(mydata[-flds[[3]],258])
z = qda(x_star,vect)
x_pred=t(H)%*%t(mydata[flds[[3]],2:257])
x_star_pred = t(x_pred)
vect_pred=as.vector(mydata[flds[[3]],258])
pred = predict(z,x_star_pred)$class
summary(pred == vect_pred)

#4
r = multinom(formula = g~.-speaker-row.names, data = mydata[-flds[[4]],],MaxNWts=3000)
beta = summary(r)$coefficients
#H = bs(beta[2:257],df = 12)
H = bs(beta[2:257],df = 12, knots=c(25,50,75,100,125,150,175,200,225,250))
#H = bs(beta[2:257],df = 24)
#H = bs(beta[2:257],df = 36)
#H = bs(beta[2:257],df = 48)
x= t(H)%*%t(mydata[-flds[[4]],2:257])
x_star = t(x)
vect=as.vector(mydata[-flds[[4]],258])
z = qda(x_star,vect)
x_pred=t(H)%*%t(mydata[flds[[4]],2:257])
x_star_pred = t(x_pred)
vect_pred=as.vector(mydata[flds[[4]],258])
pred = predict(z,x_star_pred)$class
summary(pred == vect_pred)

#5
r = multinom(formula = g~.-speaker-row.names, data = mydata[-flds[[5]],],MaxNWts=3000)
beta = summary(r)$coefficients
#H = bs(beta[2:257],df = 12)
#H = bs(beta[2:257],df = 12, knots=c(25,50,75,100,125,150,175,200,225,250))
#H = bs(beta[2:257],df = 24)
#H = bs(beta[2:257],df = 36)
H = bs(beta[2:257],df = 48)
x= t(H)%*%t(mydata[-flds[[5]],2:257])
x_star = t(x)
vect=as.vector(mydata[-flds[[5]],258])
z = qda(x_star,vect)
x_pred=t(H)%*%t(mydata[flds[[5]],2:257])
x_star_pred = t(x_pred)
vect_pred=as.vector(mydata[flds[[5]],258])
pred = predict(z,x_star_pred)$class
summary(pred == vect_pred)

#6
r = multinom(formula = g~.-speaker-row.names, data = mydata[-flds[[6]],],MaxNWts=3000)
beta = summary(r)$coefficients
#H = bs(beta[2:257],df = 12)
H = bs(beta[2:257],df = 12, knots=c(25,50,75,100,125,150,175,200,225,250))
#H = bs(beta[2:257],df = 24)
#H = bs(beta[2:257],df = 36)
#H = bs(beta[2:257],df = 48)
x= t(H)%*%t(mydata[-flds[[6]],2:257])
x_star = t(x)
vect=as.vector(mydata[-flds[[6]],258])
z = qda(x_star,vect)
x_pred=t(H)%*%t(mydata[flds[[6]],2:257])
x_star_pred = t(x_pred)
vect_pred=as.vector(mydata[flds[[6]],258])
pred = predict(z,x_star_pred)$class
summary(pred == vect_pred)

#7
r = multinom(formula = g~.-speaker-row.names, data = mydata[-flds[[7]],],MaxNWts=3000)
beta = summary(r)$coefficients
#H = bs(beta[2:257],df = 12)
#H = bs(beta[2:257],df = 12, knots=c(25,50,75,100,125,150,175,200,225,250))
#H = bs(beta[2:257],df = 24)
#H = bs(beta[2:257],df = 36)
H = bs(beta[2:257],df = 48)
x= t(H)%*%t(mydata[-flds[[7]],2:257])
x_star = t(x)
vect=as.vector(mydata[-flds[[7]],258])
z = qda(x_star,vect)
x_pred=t(H)%*%t(mydata[flds[[7]],2:257])
x_star_pred = t(x_pred)
vect_pred=as.vector(mydata[flds[[7]],258])
pred = predict(z,x_star_pred)$class
summary(pred == vect_pred)

#8
r = multinom(formula = g~.-speaker-row.names, data = mydata[-flds[[8]],],MaxNWts=3000)
beta = summary(r)$coefficients
#H = bs(beta[2:257],df = 12)
H = bs(beta[2:257],df = 12, knots=c(25,50,75,100,125,150,175,200,225,250))
#H = bs(beta[2:257],df = 24)
#H = bs(beta[2:257],df = 36)
#H = bs(beta[2:257],df = 48)
x= t(H)%*%t(mydata[-flds[[8]],2:257])
x_star = t(x)
vect=as.vector(mydata[-flds[[8]],258])
z = qda(x_star,vect)
x_pred=t(H)%*%t(mydata[flds[[8]],2:257])
x_star_pred = t(x_pred)
vect_pred=as.vector(mydata[flds[[8]],258])
pred = predict(z,x_star_pred)$class
summary(pred == vect_pred)

#9
r = multinom(formula = g~.-speaker-row.names, data = mydata[-flds[[9]],],MaxNWts=3000)
beta = summary(r)$coefficients
#H = bs(beta[2:257],df = 12)
#H = bs(beta[2:257],df = 12, knots=c(25,50,75,100,125,150,175,200,225,250))
#H = bs(beta[2:257],df = 24)
#H = bs(beta[2:257],df = 36)
H = bs(beta[2:257],df = 48)
x= t(H)%*%t(mydata[-flds[[9]],2:257])
x_star = t(x)
vect=as.vector(mydata[-flds[[9]],258])
z = qda(x_star,vect)
x_pred=t(H)%*%t(mydata[flds[[9]],2:257])
x_star_pred = t(x_pred)
vect_pred=as.vector(mydata[flds[[9]],258])
pred = predict(z,x_star_pred)$class
summary(pred == vect_pred)

#10
r = multinom(formula = g~.-speaker-row.names, data = mydata[-flds[[10]],],MaxNWts=3000)
beta = summary(r)$coefficients
#H = bs(beta[2:257],df = 12)
H = bs(beta[2:257],df = 12, knots=c(25,50,75,100,125,150,175,200,225,250))
#H = bs(beta[2:257],df = 24)
#H = bs(beta[2:257],df = 36)
#H = bs(beta[2:257],df = 48)
x= t(H)%*%t(mydata[-flds[[10]],2:257])
x_star = t(x)
vect=as.vector(mydata[-flds[[10]],258])
z = qda(x_star,vect)
x_pred=t(H)%*%t(mydata[flds[[10]],2:257])
x_star_pred = t(x_pred)
vect_pred=as.vector(mydata[flds[[10]],258])
pred = predict(z,x_star_pred)$class
summary(pred == vect_pred)
