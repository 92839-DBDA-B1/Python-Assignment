# 6. Write a Python program that filters out all strings that have more than 5 characters from a list of strings using the filter() function.
# Input : words = ['Red', 'Green', 'Yellow', 'Purple', 'Orange']
# Output : ['Yellow','Purple','Orange']

words = ['Red', 'Green', 'Yellow', 'Purple', 'Orange']
def function(words):
    list1=list(filter(lambda n:len(n)>5,words))
    print(list1)

function(words)
