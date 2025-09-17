# 6. Find all of the numbers from 1-1000 that are divisible by 7. Solve Using list Comprehension.

def function():
    list2=[x for x in range(1,1000) if x%7==0]
    print(list2)

function()