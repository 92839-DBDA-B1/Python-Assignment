# 10) Write a Python program to count the elements in a list until an element is a
# tuple.
# Sample input : list = [10, 20, 30, (40,50), 60]
# Sample output = 3

list = [10, 20, 30, (40,50), 60]
def ruturn_count(list):
    a=0
    for i in list:
        if isinstance(i,tuple):
            break
        else:
            a=a+1
    print(a)

ruturn_count(list)


