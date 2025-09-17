# 7) Write a program to read 6 numbers and create a dictionary having keys EVEN and ODD.
#   Dictionary's value should be stored in list. Your dictionary should be like:
#   {'EVEN':[8,10,64], 'ODD':[1,5,9]}


def function():
    list1=[]
    for i in range(0,6):
        num=int(input("Enter a number:"))
        list1.append(num)
    
    print("Your Entered numbers are:",list1)
    list2=lambda n:n%2==0
    list3=lambda n:n%2!=0
    even=list(filter(list2,list1))
    odd=list(filter(list3,list1))
    print("EVEN:",even)
    print("ODD",odd)
function()

