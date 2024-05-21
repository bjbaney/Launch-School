# Reassignments in Python
# can't use augmented assignments as a function argument or a return vale
# With lists
bar = [1, 2, 3] # bar is [1, 2, 3]
bar += [4, 5] # bar is now [1, 2, 3, 4, 5]

# With sets
bar = {1, 2, 3}
# bar |= [4, 5] # | performs a set union
              # bar is now {1, 2, 3, 4, 5}
bar -= {2, 4} # bar is now {1, 3, 5}

# Exercises
# 1. Classify the following potential non-constant variable names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice
    # idiomatic
    # non-idiomatic <-- uses PascalCase instead of snake_case
    # idiomatic
    # non-idiomatic <-- uses snake_case, but capitalizes the first letter of the second word
    # illegal <-- can't start with a number
    # idiomatic
    # non-idiomatic <-- other than constants, variables shouldn't use all capital letters
    # non-idiomatic <-- pi symbol is not an ASCII character

# 2. Classify the following potential function names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice
    # idiomatic
    # non-idiomatic <-- uses pascal case
    # idiomatic
    # non-idiomatic <-- shouldn't use capital letters
    # illegal <-- can't start with a number
    # idiomatic
    # non-idiomatic <-- shouldn't use all capitals, those are used for constants
    # non-idiomatic <-- pi symbol is not an ASCII character

# 3. Classify the following potential constant variable names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice
    # non-idiomatic <-- should use all caps for constants
    # non-idiomatic <-- don't use pascal, use all caps
    # non-idiomatic <-- this is a regular variable
    # idiomatic
    # illegal <-- can't start with numbers
    # non-idiomatic <-- should use all caps for constants
    # idiomatic
    # non-idomatic <-- pi symbol is not an ASCII character

# 4. Classify the following potential class names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice
    # non-idiomatic <-- should use pascal case
    # idiomatic
    # non-idiomatic <-- use pascal case
    # illegal <-- can't start with numbers
    # non-idiomatic <-- use pascal case
    # idiomatic
    # non-idiomatic <-- pi symbol is not an ASCII character

# 5. Write a program named greeter.py that greets 'Victor' three times. Your program should use a variable and not hard code the string value 'Victor' in each greeting
name = 'Victor'
morning = 'Good Morning, '
afternoon = 'Good Afternoon, '
evening = 'Good Evening, '
# print(morning + name)
# print(afternoon + name)
# print(evening + name)

# 6. Write a program named age.py that includes someone's age and then calculates and reports the future age 10, 20, 30, and 40 years from now.
age = 30
# print(f'You are {age} years old.')
# print(f'In 10 years you will be {age + 10} years old.')
# print(f'In 20 years you will be {age + 20} years old.')
# print(f'In 30 years you will be {age + 30} years old.')
# print(f'In 40 years you will be {age + 40} years old.')

# 7. What happens when you run the following code? Why?
# it will run all of the print messages for Victor, and then run them all for Nina afterwards. The code is read like a book, so it starts at the top, sees name assigned to Victor
# so it prints all of the print statements for Victor, then sees the name as Nina as it continues exectuting code going down, so prints all the ones with Nina. 

# 8. Assume you have $1,000.00 in the bank, and you've somehow managed to find a bank that pays you 5% (this is a wish-fulfillment fantasy) compounded interest every year. Do this for 5 years
balance = (1000 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05)
# print(balance)

# 9. Repeat the previous question but, this time, use augmented assignment to compute the final result, one year at a time
balance = 1000
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
# print(balance)

# 10. Assume that obj already has a value of 42 when the code starts running. Which of the subsequent statements reassign the variable? Which statements mutate the value of the object
# that obj references? Which statements do neither?
obj = 'ABcd'
obj.upper() # neither
obj = obj.lower() # reassign
print(len(obj)) # neither
obj = list(obj) # mutates <-- this one is reassignment not mutation
obj.pop() # mutates
obj[2] = 'X' # mutates
obj.sort() # neither <-- this one is mutation
set(obj) # mutates <-- neither
obj = tuple(obj) # mutates <-- this one is reassignment