# 1) Given a dictionary of students and their favourite colours:
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
# A. Find out how many students are in the list
# B. Change Lisa’s favourite colour
# C. Remove 'Jenny' and her favourite colour
# D. Sort and print students and their favourite colours alphabetically by name

people={'Arham':'Blue','Vinod':'Purple','Lisa':'Yellow','Jenny':'Pink'}

# A. Find out how many students are in the list
n=len(people)
print(n)

people['Lisa']='Red'
print(people)

del people['Jenny']
print(people)

list2=dict(sorted(people.items()))
# dict1=dict(list2)
print(list2)