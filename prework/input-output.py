# name = 'Jane'
# print(f'Good morning, {name}!')

# by default, multiple items are separated by spaces, can use the sep keyword to use a different separator
# print([1, 2, 3], 4, False, { 5, 6, 8, 9 }, sep='')

# Terminal Input
# Python has a built-in function called input() that lets Python programs read input from the terminal
# print("What's your name?")
# name = input()
# print(f'Good morning, {name}!')

# You can also use input() function to display the prompt the user sees:
# name = input("What's your name? ")
# print(f'Good morning, {name}!')

# num1 = input('Enter the first number: ')
# num2 = input('Enter the second number: ')
# sum = int(num1) + int(num2)
# print(f'The numbers {num1} and {num2} add to {sum}')

# Exercises
# 1. Write a program named greeter.py. The program should ask for your name, then output Hello, name, where name is the name you entered
# name = input("What is your name? ")
# print(f'Hello, {name}!')

# 2. Modify greeter.py program to ask for the user's first and last names separately, then greet the user by their full name
# first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")
# full_name = first_name + " " + last_name
# print(f'Hello, {full_name}!')

# 3. Write a program named age.py that asks users to enter their age, then calculates and reports the furture age 10, 20, 30, and 40 years from now
age = input("How old are you? ")
print(f'You are {age} years old.')
age = int(age)
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')