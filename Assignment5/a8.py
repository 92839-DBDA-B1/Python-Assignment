# 8) Write a function translate() that will translate a text into "rövarspråket"
#   (Swedish for "robber's language"). That is, double every consonant and place an
#   occurrence of "o" in between. For example, translate("this is fun") should return
#   the string "tothohisos isos fofunon".

def function():
    str1=input("Enter a sting:")
    str2=str1.split(" ")
    str4=[]
    str6=[]
    for i in str2:
        str3=list(i)
        str4.append(str3)
    print(str4)
    for i in str4:
        str5=[]
        for j in i:
            if j in 'aeiouAEIOU':
                str5.append(j)
            else:
                str5.append(j+"o"+j)

        str6.append(''.join(str5))
    print(str6)
    result = ' '.join(str6)  # join words into final string
    print(result)

function()
