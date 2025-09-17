# 5) Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise.
a=[10,20,30,40,50]
b=[50,60,70,80,90]

def overlapping(a,b):
    list1=[value for value in a if value in b]
    if list1:
        return True
    else:
        return True
istrue=overlapping(a,b)
print(istrue)