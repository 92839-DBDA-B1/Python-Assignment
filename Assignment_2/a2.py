# 2) Write a program that accepts a list from user and print the alternate element of list.

list=[]

for i in range(0,10):
    add=int(input("Enter the nuber:"))
    list.append(add)

print("List=",list)

for i in range(0,10,2):
    print(i)
    