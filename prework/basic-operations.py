# Arithmetic Operations
# Division ---- diving with just / will always end up as a floating number
16 / 4 # this would equal 4.0

# When you divide two ints, floats, or one with each, / is always a float. Using // would return the largest whole number less than or equal to the floating point result
# If the operand is a float, the return value will also be a float, but will be rounded to the nearest whole number still
16 // 3 # would give you 5

# Exponents
16**3 # would give 4096

# Floating Point Imprecision
# Floating point numbers have some precision issues, for instance if you add 0.1 and 0.2, and compare that result to 0.3, you will get False
0.1 + 0.2 == 0.3 # false
# This can cause serious problems in some applications, such as finance. One way around this problem in Python is to use math.isclose
import math
math.isclose(0.1 + 0.2, 0.3) # True
# You can also use decimal.Decimal type to make precise computations
from decimal import Decimal
Decimal('0.1') + Decimal('0.2') == Decimal('0.3') # True

# Equality Comparison
42 == 42 # True
42 == 43 # False
'foo' == 'foo' # True
'FOO' == 'foo' # False
42 != 42 # False
42 != 43 # True
'foo' != 'foo' # False
'FOO' != 'foo' # True

# Concatenation
'abc' * 3 # Would give you abcabcabc

# Coercion <-- would be considered as explicit coercion when using str, int, etc to coerce values from one type to the other
int('5') # Would turn to the int 5
float('3.141592') # Would turn to the float 3.141592
str(5) # '5'
str(3.141592) # '3.141592'

# Implicit Coercion <-- Python has this. When you use the print() to print an object -- any object -- print will implicitly coerce it to a string before printing it
# explicit
print(str(3))
print(str([1, 2, 3]))
# implicit
print(3)
print([1, 2, 3])

# Determining Types
type(1) # <class 'int'>
type('abc').__name__ # str
type('abc') is str # True

# all 3 of the above approaches discount the effects of inheritance. You may want to consider using the isinstance function, which determines whether an object
# is an instance of a particular type. It takes inheritance into account
isinstance('abc', str) # True

class A:
    pass

class B(A):
    pass

b = B()

type(b).__name__ # B
type(b) is B # True
type(b) is A # False <-- b's type is not A
isinstance(b, B) # True
isinstance(b, A) # True, b is instance of A and B

# String Representations
# str() is intended to return something humans can read, and python implicitly calls str() when it needs to print or interpolate a value. 
# repr is a bit lower-level. It returns a string that you can, in theory, use to create a new instance of an object.
# For most built-in types, str and repr return the same value. However, that is not always the case. Strings are one of the more obvious types with different str and repr values:
my_str = 'abc'
# print(my_str) # prints abc
# print(str(my_str)) # prints abc
# print(repr(my_str)) # Prints 'abc' note the quotes

# Collection and String Lengths
# print(len('Launch School')) # 13 
# print(len(range(5, 15))) # 10
# print(len(['a', 'b', 'c'])) # 3

# Indexing and Key Access
my_list = [1, 2, 3, 4]
my_list[2] = 6
# print(my_list)

my_dict = {
    'dog': 'barks',
    'cat': 'meows',
    'pig': 'oinks',
}

my_dict['pig'] = 'snorts'

# adds a new key:value pair to the dict
my_dict['fish'] = 'glub glub'

# Exercises
# 1. Concatenate two strings, one with your first name and one with your last name, to create a new string with your full name. 
first_name = 'Billy '
last_name = 'Baney'
full_name = first_name + last_name

# 2. Use the REPL and the arithmetic operators to extract the individual digits of 4936
number = 4936
ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10

# 3. What does the following code do? Why?
# '5' + '10' will give you '510' because the numbers are strings instead of integers, so it concats them.

# 4. Refactor the code from the previous exercise to use coercion to print 15 instead
int('5') + int('10')

# 5. Will an error occur if you try to access a list element with an index greater than or equal to the list's length? For example:
foo = ['a', 'b', 'c']
print(foo[3]) # will this result in an error?
# Yes, this will result in an error because foo[3] doesn't exist, it's longer than the length of the list

# 6. To what does the following expression evaluate?
'foo' == 'Foo' # <-- this will evaluate to false, because foo doesn't equal Foo due to it having a capital F.

# 7. What will the following code do? Why?
int('3.1415') # Will result in an error, since 3.1415 can't be a whole number

# 8. To what value does the following expression evaluate?
'12' < '9' # <-- This will be true because '9' is greater than the '1'