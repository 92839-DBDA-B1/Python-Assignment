# 1 . A pangram is a sentence that contains all the letters of the English alphabet at least once.
# for example: The quick brown fox jumps over the lazy dog. 
# Your task here is to write a function to check a sentence to see if it is a pangram or not.

def function():
    str1=input("Enter a sentence:")
    if 'a' and 'b' and 'c' and 'd' and 'e' and 'f' and 'g' and 'h' and 'i' and 'j' and 'k' and 'l' and 'm' and 'n' and 'o' and 'p' and 'q' and 'r' and 's' and 't' and 'u' and 'v' and 'w' and 'x' and 'y' and 'z' in str1.lower():
        print("Sentence is pangram")
    else:
        print("Sentence is not pangram")
    
function()

