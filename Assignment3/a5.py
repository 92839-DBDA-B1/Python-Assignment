# 5. Write a Python program that adds two lists element-wise using the map() function.
#     input :   list1 = [1, 2, 3, 4, 5]
#               list2 = [5, 4, 3, 2, 1]
#     Expected Output  : [6, 6, 6, 6, 6]

list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

def function(list1,list2):
    list3=list(map(lambda a,b:a+b,list1,list2))
    print(list3)

function(list1,list2)