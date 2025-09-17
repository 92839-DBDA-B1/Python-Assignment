#4] Write a program to accept three integer numbers and find its average.


num1=int(input("Enter numer:"))
num2=int(input("Enter numer:"))
num3=int(input("Enter numer:"))

avg=lambda num1, num2, num3:(num1+num2+num3)/3
print(f"Average of three numbers: {avg(num1, num2, num3)}")
