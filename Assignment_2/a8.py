# 8) Write a program that will calculate the price for a quantity entered from the keyboard, given that the unit price is Rs 5 and there is a discount of 10 percent for quantities over 30 and a 15
# percent discount for quantities over 50.

num=int(input("Enter a quantity:"))

def function(num):
    reues=num*5
    print("Rupay=",reues)
    discount=0
    if num>50:
        discount=(reues)*(15/100)
        price=reues-discount      
    elif num>30:
        discount=reues*(10/100)
        price=reues-discount
    else:
        price=reues-discount
    print("Price=",price)

function(num)