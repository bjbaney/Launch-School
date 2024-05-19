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
# print(f'5 plus 5 equals {5 + 5}.')
my_name = "Billy"
# print(f"My name is {my_name}.")

# How to print long numbers with commas in f strings
# print(f'{9123456789:,}')

# Sequences
# represent an ordered collection of objects. A sequences objects can be accessed using a numeric index. In many other languages, the best known sequence is the array.
# Python uses lists to fill the same role, but tuples and ranges are also important

#LISTS ARE MUTABALE TUPES ARE IMMUTABLE
my_list = [1, 'xyz', True, [2, 3, 4]]


tup = ('xyz', [2, 3, 4], 1, True)
# print(tup)

# Mutating Lists
my_list[3] = 'New Value'
# print(my_list)

# Ranges
# Sequence of integers between two endpoints. Ranges most commonly used to iterate over an increasing or decreasing range of integers
# ranges can also use [] to find an index
# print(tuple(range(1, 10, 2)))
my_range = range(5, 10)
my_range[3] # === prints the 3rd value in this range

# Maps
# Represent an unordered collection of objects stored as key:value pairs. Each key (usually a string) provides a unique identifier for a speicfic object in the map
# The dictionary (class dict) is the most common used map in Python
# A dict is a collection of key:value pairs, it is similar to a list but uses keys instead of indexes to access specific elements

# my_dict = {
#     'dog': 'barks',
#     'cat': 'meows',
#     'pig': 'oinks'
# }

# print(my_dict)

# Dictionary literals may also use a multi-line format and include lists

my_dict = {
    'title': "Monty Python's Flying Circus",
    'cast': [
        'Eric Idle',
        'John Cleese',
        'Terry Gilliam',
        'Graham Chapman',
        'Michael Palin',
        'Terry Jones',
    ],
    'first_season': 1969,
    'last_season': 1974,
    'reboot_season': None,
}
# can also use the same key to change the keys value
my_dict['first_season'] = 1970
# print(my_dict)

# Sets
# Represent an unordered collection of unique objects; the objects are sometimes called members of the set
# Sets are similar to maps, except instead of using keys and values, a set is simply a collection of immutable ( and hashable, as mentioned above ) objects

# Declaring empty set
s1 = set()

# creating a set from a literal
s2 = {2, 3, 5, 7, 11, 13}

# creating a set from a string
s3 = set('hello world!') # set members are always unique, even if you try to add duplicates. So there will always only be 1 occurrence. 

# There are two types of sets, regular sets, like above, and frozen sets (frozenset). Frozen sets are merely immutable sets
s5 = frozenset([1, 2, 3])
# you can initialize a frozen set with any iterable type, (lists, tuples, ranges)



# Exercises ===========================================================================================================\
# 1. Identify the data type or class for each of the following values:
    # 'True' === String
    # False === Boolean
    # (1, 2, 3) === Tuple
    # 1.5 === Float
    # [1, 2, 3] === List
    # 2 === Integer
    # range(5) === Range
    # {1, 2, 3} === Set
    # None === NoneType
    # {'foo': 'bar'} === Dictionary

# 2. Create a tuple called names that contains several pet names
# names = ('Oden', 'Freya', 'Albini', 'Sam', 'Brownie', 'Bear', 'Missy')
# print(names)

# 3. Create a dictionary named pets that contains a list of pet names and the type of animal
pets = {
    'Oden': 'dog',
    'Freya': 'dog',
    'Albini': 'frog',
    'Bear': 'dog'
}

print(pets)