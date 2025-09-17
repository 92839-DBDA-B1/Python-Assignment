# 4. Write a Python program that calculates the sum of the squares of all odd numbers in a list of integers using map() and filter()

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def function(numbers):
    odd=lambda n:n%2!=0
    numbers=list(filter(lambda n:n%2!=0,numbers))
    print(f"odd numbers:{numbers}")

    square_of_num=list(map(lambda n:n*n,numbers))
    print(f"square of all odd numbers:{square_of_num}")

    def add_of_square(square_of_num):
        add=0
        for i in square_of_num:
            add=add+i
        print(add)
            
    add_of_square(square_of_num)


function(numbers)



