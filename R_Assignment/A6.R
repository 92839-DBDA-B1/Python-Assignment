#6. Write a R program to create two 2x3 matrix and add,
#subtract, multiply and divide the matrixes.

m1=matrix(c(10,20,30,40,50,60),nrow=2,ncol=3,byrow=T)
m2=matrix(c(11,22,33,44,55,66),nrow=2,ncol=3,byrow=T)

add=m1+m2
print(add)
subtract=m1-m2
print(subtract)
mul=m1*m2
print(mul)
div=m1/m2