# literals - directly represent an object in source code
'Hello, world!' # str literal
3.141592 # float literal
True # boolean literal
{'a' : 1, 'b' : 2} # dict literal
[1, 2, 3] # list literal
(4, 5, 6) # tuple literal
{7, 8, 9} # set literal

# not all objets have literal forms. In those cases, we use the type constructor to create objects of the type
range(10) # range of numbers: 0 - 9
range(1, 11) # range of numbers 1 - 10
set() # empty set
frozenset([1, 2]) # Frozen set of values: 1 and 2

# Numeric Values
# integer (int) represents whole numbers, do not have a fraction or decimal part
1
2
-3
234891234
131_587_465_014_410_491

# floats represent floating point numbers, include integers and numbers with digits after the decimal point
1.0
1.4142
-3.14159
42348.912346
131_587_465.014_410_491

# Variables and Assignment
pi = 3.14159
life_the_universe_and_everything = 42
foo = "Hello, world."   #assignment or initialization
foo = "That's all, folks!"  #reassignment

# Boolean Values
# Represent binary states such as true or false
toggle_on = True   #remember in python the True is capitalized
session_active = False

# Text Sequences
# strings of characters, such as words, sentences, dates, foreign text, and so on.  Triple quoted strings are used for multi line strings
'Hello'
"He's pining for the fjords!"
"1969-07-20"
# f'{greeting}! My name is {my_name}'
# r'\w+\d+'
# print("""Hello
# my name is
# Billy.""")

# accessing individual characters of a string
my_str = 'abc'
# print(my_str[0])

#if working with a string that contains both single and double quotes, you can put it in triple quotes
# print("""My nickname is "Wolfy". What's yours?""")

# String literals
print(f'5 plus 5 equals {5 + 5}.')
my_name = "Billy"
print(f"My name is {my_name}.")

# How to print long numbers with commas in f strings
print(f'{9123456789:,}')

# Sequences
# represent an ordered collection of objects. A sequences objects can be accessed using a numeric index. In many other languages, the best known sequence is the array.
# Python uses lists to fill the same role, but tuples and ranges are also important

