# 2] Write a Python Program to Convert Celsius To Fahrenheit vice versa.
#    fahrenheit = (celsius * 1.8) + 32

celsius=int(input("Enter the Celsius:"))

def fahrenheit_calulation(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

fah=fahrenheit_calulation(celsius)
print("fahrenheit =",fah)

def celsius_calculation(fah):
    celsius=(fah-32)/1.8
    return celsius


print("celsius =",celsius)


