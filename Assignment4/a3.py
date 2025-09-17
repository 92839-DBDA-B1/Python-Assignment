# 3. Write a program in Python to remove repetitive items from a list.
# Hint Given num = [2,3,4,5,2,6,3,2]
# Expected output Result: [2, 3, 4, 5, 6] New list

def function():
    list1=[2,3,4,5,2,6,3,2]
    set1=set(list1)
    list2=list(set1)
    print(list2)

function()