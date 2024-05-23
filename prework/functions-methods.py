def hello():
    print('Hello')
    return True

# hello()
# print(hello())

# min and max
min(-10, 5, 12, 0, -20) # returns -20
max(-10, 5, 12, 0, -20) # returns 12

# ord and chr
# given a single char, ord returns an integer that repesents the Unicode point of the character
ord('a') # returns 97
ord('A') # returns 65
# chr is the exact opposite, it takes the integer and gives the corresponding character
chr(97) # returns a
chr(65) # returns A

# any and all
# They both operate on iterable collections, such as lists, tuples, ranges, dicts, and sets
# any returns true if any element in the collection in truthy, otherwise false. all returns true if ALL entries are true, else false
collection1 = [False, False, False]
collection2 = (False, True, False)
collection3 = {True, True, True}
any(collection1) # returns false
any(collection2) # returns true
any(collection3) # returns true
all(collection1) # returns false
all(collection2) # returns false
all(collection3) # returns true

# better example of this --> see if any or all elements are even:
numbers = [2, 5, 8, 10, 13]
# print(any([number % 2 == 0 for number in numbers])) # True
# print(all([number % 2 == 0 for number in numbers])) # False

# Creating Functions
def say():
    print('Output from say')

# print('First')
# say()
# print('Last')

# Scope
def well_howdy(who):
    greeting = 'Howdy'
    print(f'{greeting}, {who}')

# well_howdy('Caeley')

def add(a, b):
    return a + b

two_and_three = add(2, 3) # returns 5
# print(two_and_three)

# Functions that always return a bool value are called Predicates. For example:
def is_digit(char):
    if char >= '0' and char <= '9':
        return True
    
    return False

# Default Parameters
# def say(text='hello'):
#     print(text + '!')

# say('Howdy')
# say()

# You can provide defaults for any or all of a function's parameters, however once you specify a default value for an argument, all subsequent arguments must have default values:
# def say(msg1, msg2, msg3='dummy message', msg4):
#     pass
# SyntaxError: non-default argument follows default argument

# def say(msg1, msg2, msg3='dummy message', msg4='omitted message'): # <-- this is how it would have to look
#     pass

# Exercises
# 1. What happens when you run the following program? Why do we get that result?
# def set_foo():
#     foo = 'bar'

# set_foo()
# print(foo) # this print is outside of the function scope, it doesn't have access to the variable foo

# 2. What does this program print? Why?
# foo = 'bar'
# def set_foo():
#     foo = 'qux'

# set_foo()
# print(foo) # <-- prints 'bar' because foo is also declared as a global variable, and the function set_foo isn't printing or returning anything, so that foo is never used

# 3. Write a program that uses a multiply function to multiply two numbers and return the result. Ask the user to enter the two numbers, then output the numbers and result
# a = input("Enter the first number: ")
# b = input("Enter the second number: ")
# def multiply():
#     answer = int(a) * int(b)
#     print(f'{int(a)} * {int(b)} = {answer}')
#     return answer

# multiply()

# 4. Identify the following items in the code:
    # function name <-- multiply_numbers
    # function arguments <-- 2, 3, 4
    # function definition <-- the entire function
    # function body <-- result = num1 * num2 * num3 (next line) return result
    # function parameters <-- num1, num2, num3
    # function invocation <-- product = multiply_numbers(2, 3, 4)
    # function return value <-- return result
    # all identifiers <-- multiply_numbers, num1, num2, num3, result, product

# 5. What does the following code print?
# def scream(words):
#     return words + '!!!'
# scream('Yipeee') # <-- returns 'Yipeee!!!', doesn't print anything

# 6. What does the following code print?
# def scream(words):
#     words = words + '!!!!'
#     return
#     print(words)
# scream('Yipeee') # <-- doesn't return anything, because nothing matters after the return value, so print is never accessed.

# 7. Without running the following code, what do you think it will do?
# def foo(bar, qux):
#     print(bar)
#     print(qux)
# foo('Hello') # <-- it will give an error, it expected two arguments, not 1. 

# 8. Without running the following code, what do you think it will do?
# def foo(bar, qux):
#     print(bar)
#     print(qux)
# foo(42, 3.141592, 2.718) # <-- too many parameters, it'll throw an error

# 9. Without running the following code, what do you think it will do?
# def foo(first, second=3, third=2):
#     print(first)
#     print(second)
#     print(third)
# foo(42, 3,141592, 2,718) # <-- this program should run and print out the 3 arguments

# 10. Without running the following code, what do you think it will do?