sgn<-function(num){      #很简单的符号函数，正为1，非正为0
sgn<-rep(1,length(num))
for(i in 1:length(num)){
if(num[i]<=0){
sgn[i]<-0
}
}
sgn
}


dk<-function(x,knot){   #对应教材中的dk(x)
dk<-(sgn(x-knot)*(x-knot)^3-sgn(x-0.9)*(x-0.9)^3)/(0.9-knot)
dk
}


Nk<-function(x,knot){   #natural cubic spline的基函数
Nk<-(dk(x,knot)-dk(x,0.74))
Nk
}
povar<-function(H){     #求拟合值的var
povar<-diag(H%*%solve(t(H)%*%H)%*%t(H))
povar
}


x<-runif(50)
x<-sort(x)
H1<-matrix(c(rep(1,50),x),50,2)#样本矩阵
H2<-matrix(c(rep(1,50),x,x^2,x^3),50,4)
H3<-matrix(c(rep(1,50),x,x^2,x^3,sgn(x-0.33)*(x-0.33)^3,sgn(x-0.66)*(x-0.66)^3),50,6)
H4<-matrix(c(rep(1,50),x,Nk(x,0.1),Nk(x,0.26),Nk(x,0.42),Nk(x,0.58)),50,6)
plot(povar(H1)~x,type="b",col="orange",pch=16,ylim=c(0,0.6),ylab="Pointwise Variances")
mtext(text="orange--Global Linear",side=3,line=-1)
par(new=T)
plot(povar(H2)~x,type="b",col="red",pch=16,ylim=c(0,0.6),ylab="Pointwise Variances")
mtext(text="red--Global Cubic Polynomial",side=3,line=-2)
par(new=T)
plot(povar(H3)~x,type="b",col="green",pch=16,ylim=c(0,0.6),ylab="Pointwise Variances")
mtext(text="green--Cubic Spline - 2 knots",side=3,line=-3)
par(new=T)
plot(povar(H4)~x,type="b",col="blue",pch=16,ylim=c(0,0.6),ylab="Pointwise Variances")
mtext(text="blue--Natural Cubic Spline - 6 knots",side=3,line=-4)


