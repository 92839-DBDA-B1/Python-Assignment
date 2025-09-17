# 2) Write a program to sum all the values of a dictionary.
# Hint dict1 = {‘key 1’: 200, ‘key 2’: 300,}
# Expected output
# Result: 500

def function():
    dict1 = {'key 1': 200, 'key 2': 300,'key 3':400}
    num=0
    for i in dict1.values():
        num=num+i

    print(num)
function()
    