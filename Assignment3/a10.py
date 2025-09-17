
# 11.  Write a Python program that filters out all palindromes from a list of strings using the filter() function.
# words = ['level', 'radar', 'hello', 'world', 'madam']
words = ['level', 'radar', 'hello', 'world', 'madam']
def function(words):
    is_pelindrom=lambda n:n[: :-1]==n[::]
    list1=list(filter(is_pelindrom,words))
    print(list1)

function(words)