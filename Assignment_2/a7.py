# 7) Write a function filter_long_words() that takes a list of words and an integer len and returns the list of words that are longer than len.


words=[]
for i in range(0,4):
    i=input("Enther a word:")
    words.append(i)

print("Words list=",words)

lent=int(input("Enter a length:"))
print(lent)

def filter_long_words(words,lent):
    for i in words:
        a=len(i)
        if a>=lent:
            print(i)

filter_long_words(words, lent)

