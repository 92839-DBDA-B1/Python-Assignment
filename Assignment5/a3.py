# 3) Define a function subtract() that takes two lists and returns difference (i.e. excess elements from list1). If list1 = [10, 20, 30, 40] and list2 = [30, 40, 50, 60], then result should be [10, 20].

def function():
    list1 = [10, 20, 30, 40]
    list2 = [30, 40, 50, 60]
    set1=set(list1)
    set2=set(list2)
    list3=list(set1.difference(set2))
    print(list3)

function()