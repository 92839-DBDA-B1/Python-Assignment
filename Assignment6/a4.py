
# 4. Calculate the sum and average of the digits present in a string Str1="Python83737@#8496"
# expected Output : sum = 55
#                    avg = 6.111
import re
def function():
    num2=0
    l3=[]
    l4=[]
    str1="Python83737@#8496"
    l1=re.findall(r'[0-9]+',str1,re.I)
    print(l1)
    for i in l1:
        l2=(list(i))
        l3+=l2
    print(l3)
    for i in l3:
        l4.append(int(i))
    print(l4)
    sum=0
    for i in l4:
        sum=sum+i
    
    print("sum=",sum)
    avg=sum/len(l4)
    print(f"avg = {avg:.3f}")
function()