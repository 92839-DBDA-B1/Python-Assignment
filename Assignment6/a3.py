# 3. Write a program that display following output:
#  SHIFT
#  HIFTS
#  IFTSH
#  FTSHI
#  TSHIF
#  SHIFT

def function():
    str1="SHIFT"
    print("SHIFT")
    for _ in range(0,len(str1)):
        str1=str1[1:]+str1[0]
        print(str1)
function()