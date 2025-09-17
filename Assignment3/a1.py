# 1. Write a Python program that finds the longest word in a list of strings. Use map() to calculate the length of each word, and filter() to get the word with the maximum length.
   
# words = ["python", "functional", "programming", "is", "powerful"]
words = ["python", "functional", "programming", "is", "powerful"]

def function(words):
    calculate_len=lambda n:len(n)
    lent=list(map(calculate_len,words))
    print(lent)

    max_len=max(lent)
    max_word=lambda n:len(n)==max_len
    word=list(filter(max_word,words))
    print("Maximam length word: ",word)

function(words)
