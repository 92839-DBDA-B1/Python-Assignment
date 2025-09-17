# 8. Write a Python Program to find the repeated item of a tuple(Take a value
# #from user which you want to find)

# tuple1 = (12,13,14,16,18,20,21,14,18,14)

list1=[]
for i in range(0,9):
    num=int(input("Enter a numbers:"))
    list1.append(num)

print("Enered values:",list1)
tup=tuple(list1)

def function(tup):
    list2=[x for x in tup if tup.count(x)>1 in tup]
    print(list2)

function(tup)