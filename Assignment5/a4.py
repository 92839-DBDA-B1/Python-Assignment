# 4) In following text count occurrence of each letter (irrespective of case). Hint: convert string to same case e.g. text.lower(). Do not use Counter collection.

# text = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming."""

def function():
    text = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming."""
    text2=text.split(" ")
    print(text2)

    word_count={}
    for word in text2:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1


    print(word_count)
function()