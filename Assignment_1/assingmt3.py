# 3] Write a program to accept a 4 digit number and
#    a. Display face value of each decimal digit
#    b. Display place value of each decimal digit
#    c. Display no in reverse order by changing decimal place values.
   
#    If user enters a 4 digit number 9361 output should be
#    a. 9 3 6 1
#    b. 9361 = 9 000 + 300 + 60 + 9
#    c. 1639


num=int(input("Enter the number:"))

def face_Value(num):
    digit=1000
    while(num>0):
        num1=int(num//digit)
        print(num1,end=" ")
        num=num%digit
        digit=digit/10

face_Value(num)
print( " ")
def Place_Value(num):
    digit=1000
    while(num>0):
        num1=int(num//digit)
        num2=num1*digit
        print(num2,end="  ")
        num=num%digit
        digit=digit//10

Place_Value(num)
print( " ")
def reverce(num):
    digit=10
    while(num>0):
        num1=num%digit
        print(num1,end="")
        num=num//digit

reverce(num)



    