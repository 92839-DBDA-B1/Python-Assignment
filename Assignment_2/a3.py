# 3) Replace single element ‘b’ in given list [’a’, ’b’, ’c’, ’d’, ’e’] with [1, 2, 3].

list=['a','b','c','d','e']
pos=list.index('b')
list[pos]=[1,2,3]
print(list)