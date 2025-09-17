#1] Write a Python Program find an area of a rectangle and perimeter of the rectangle.

len=int(input("Enter the length:"))
brd=int(input("Enter the breadth:"))

def area_of_rectangle(len,brd):
    are=len*brd
    return are

def perimeter_of_rectangle(len,brd):
    prm=2*(len*brd)
    return prm

area=area_of_rectangle(len,brd)
perimeter=perimeter_of_rectangle(len,brd)

print(f"Area of Rectangle:{area}")
print(f"Perimeter of Rectangle:{perimeter}")