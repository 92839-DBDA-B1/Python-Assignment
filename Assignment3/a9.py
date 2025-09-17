# 10. Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
# For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******

def histogram():
    list1=[]
    for i in range(0,4):
        num=int(input("Enter a number:"))
        list1.append(num)
    print("Entered numers:",list1)

    for i in list1:
        print("*" *i)

histogram()