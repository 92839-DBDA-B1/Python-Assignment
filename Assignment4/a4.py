# 4. Python program to create a list of tuples from given list having number and its cube in each tuple.
# I/P-[1,2,5,6]  Output-[(1, 1), (2, 8), (5, 125), (6, 216)]

def function():
    list1=[1,2,5,6]
    cube = lambda n : (n,n**3)
    result = list(map(cube,list1))
    print(result)

function()


