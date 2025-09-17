# 3. Write a Python program to convert a given list of integers and a tuple of integers into a list  of strings.Use Python map.
list1=[1,2,3,4,5,6,7,8,9]
tuple2=1,2,3,4,5,6,7,8,9
def function(list1):
    string="".join(map(str,list1))

    print(f"string={string},type={type(string)}")

function(list1)

def function1(tuple2):
    string="".join(map(str,tuple2))

    print(f"string={string},type={type(string)}")

function1(tuple2)