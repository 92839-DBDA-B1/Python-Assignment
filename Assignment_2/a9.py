# 9)  Concatenate two lists in the following order by using list comprehension
# Input:- list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Output:- [’Hello Dear’, ’Hello Sir’, ’take Dear’, ’take Sir’]

list1=[]
list2=[]

for i in range(0,2):
    a=input("Enter list1 caracter:")
    list1.append(a)

print("List1=",list1)

for i in range(0,2):
    a=input("Enter list1 caracter:")
    list2.append(a)

print("List1=",list2)

def function(list1,list2):
    list3=[x +" "+ y for x in list1 for y in list2 ]
    print(list3)

function(list1,list2)