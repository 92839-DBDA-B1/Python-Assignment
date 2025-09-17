# 5. Create a list of tuples where each tuple contains a number and its square for numbers from 0 to 9. Solve using list comprehension.

def function():
    list1=lambda n:(n,n**2)

    list2=list(map(list1,range(0,9+1)))
    print(list2)

function()