# 9) Write a version of a palindrome recognizer that also accepts phrase
# palindromes such as "Go hanga salami I'm a lasagna hog.", 
# "Was it a rat I saw?", 
# "Step on no pets", 
# "Sit on a potato pan, Otis", 
# "Lisa Bonet ate no basil", 
# "Satan, oscillate my metallic sonatas", 
# "I roamed under it as a tired nude Maori",
# "Rise to vote sir", or the exclamation "Dammit, I'm mad!".
# Note that punctuation, capitalization, and spacing are usually ignored.
import re
def function():
    stri1=input("Enter a string:")
    stri1=re.findall(r'[a-zA-Z]',stri1)
    str3=''.join(stri1).lower()
    print(str3)
    if str3[::]==str3[::-1]:
        print("String is palindrom!")
    else:
        print("String is not palindrom!")
        
    # str2=stri1.lower()
    # print(str2)
    # str2=str2.replace(" ","")
    # print(str2)
    # str2=str2.
function()