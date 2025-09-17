# 9] Write a program that prompts the user to input a year and determine whether the year is a leap  year or not. Leap Years are any year that can be evenly divided by 4.
#    A year that is evenly divisible by 100 is a leap year only if it is also evenly divisible by    400.
#    Example :
#    1992 Leap Year
#    2000 Leap Year
#    1900 NOT a Leap Year
#    1995 NOT a Leap Year

year=int(input("Enter year:"))

if year%4==0: 
    if ((year%4==0) and (year%100!=0)) or (year%400==0):
        print("Year is leap year")
    else:
        print("Year is not leap year")
        
        
        
    