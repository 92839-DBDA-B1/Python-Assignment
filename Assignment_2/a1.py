# 1) Using for loop, write and run a Python program to find factorial from 0 to 10.
facto=int(input("Enter a number:"))

def factorial(facto):
    n=1
    for i in range(1,facto+1):
        if facto==0:
            return 0
        else:
            n=n*i
    return n

num=factorial(facto)
print(num)