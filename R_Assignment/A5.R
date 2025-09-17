#5. Write a R program to access the element at 3rd column and 2nd row, 
#only the 3rd row and only the 4th column of a given matrix(c(1:16)) and Give row_names ,col_names.

dimensatio =list(c('Python',"Java","DBMS","HTML"),
                 c("DBDA","DAC","DMC","DITTS"))
numbers=matrix(c(1:16),nrow = 4,ncol=4,byrow=T,dimnames = dimensatio)
print((numbers))
print(numbers[2,3])
print(numbers['Java','DMC'])
print(numbers[3,4])
print(numbers['DBMS','DITTS'])