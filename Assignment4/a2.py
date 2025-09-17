# 2.Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.

# Orginal list:
# [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

# Numbers of the above list divisible by nineteen or thirteen:
# [19, 65, 57, 39, 152, 190]

def function():
    list1=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
    list2=lambda n:((n%13)==0 or (n%19)==0)
    list3=list(filter(list2,list1))
    print(list3)

function()
