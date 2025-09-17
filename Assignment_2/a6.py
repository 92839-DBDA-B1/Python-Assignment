# 6) Find and display the largest number of a list without using built-in function max(). Your program should ask the user to input values in list from keyboard.

list=[]

for i in range(0,10):
    a=int(input("Enter the number:"))
    list.append(a)

print("list=",list)
b=0
for i in list:
    if b<=i:
        b=i
print(b)
