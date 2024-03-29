
####################################################################################
# İntroduction & Quick recap
####################################################################################

# Numbers: Integers
x = 46
type(x) # Output : int

# Numbers: Float
x = 10.3
type(x) # Output : float

# Numbers: Complex
x = 3j + 1
type(x) # Output : complex

# Strings
x = "Hello AI era"
type(x) # Output : str

# Boolean
True
False
type(21 > 20) # Output : bool

# Lists
x = ["btc", "eht", "xrp"]
type(x) # Output : list

# Dictionary
# <dict_name> = {key-1: value-1, key-2: value-2, ... , key-n: value-n}
x = {"name": "Peter", "Age": 36}

# Tuple
x = ("python", "ml", "ds")
type(x) # Output : tuple

# Sets
x = {"python", "ml", "ds"}
type(x) # Output : set

# Note: Lists, Tuples and Dictionary data structures are also called "Python Collections" 


####################################################################################
# Numbers
####################################################################################
a = 5
b = 10.5 # type is float

a * 3
a / 7
a * b / 10
a ** 2 # output: 25

# Change types of variables
int(b) # output: 10
float(a) # output: 5.0
int(a * b / 10) # output: 5


####################################################################################
# Strings
####################################################################################
print("John") # print('John') are the same
name = "John"

# if we have many rows:
long_str = """ Data Structures:
Numbers: Int, Float, Double;
Characters (Strings): str;
List; Dictionary; Tuple; Set;
Boolean: bool"""
print(long_str)

# Choose an element of any string
name[0] # output: 'J'
name[3] # output: 'n'

# Slicing in seris of characters
name[0:2] # output: 'Jo'
name[:2] # output: 'Jo'

long_str[:10] # output: ' Data Stru'

# Querying a character in a String
"Data" in long_str # output: True
'struct' in long_str # output: False
"bool" in long_str # output: True


####################################################################################
# String methods
####################################################################################
# identify methods that belong to a specific ds
dir(str)

# len method
name = "John"
type(name) # output: str
type(len) # output: builtin_function_or_method

len(name) # output: 4
len("sample sentence for len function") # output: 32
# note: Distiguishing method and function
# e.g len is a function

# upper() and lower() methods
"miuul".upper() # 'MIUUL'
"miuul".isupper() # False

"MIUUL".lower() # 'miuul'
"MIUUL".islower() # False

# type(upper) # output:
# name 'upper' is not defined. Did you mean: 'super'?
# upper() is also a method


# Replace method
hi = "Hello AI era"

# <string>.replace(<target>, <new_character>)
hi.replace("l", "p") # output: 'Heppo AI era'
hi.replace("llo", "y") # output: 'Hey AI era'

# Split method
'Hello AI era'.split() # output: ['Hello', 'AI', 'era']
'Hello AI era'.split("l") # output: ['He', '', 'o AI era']

# Strip method. Default: space
"     ofofo   ".strip() # output: 'ofofo'
'ofofoo'.strip("o") # output: 'fof'

'foo'.capitalize() # output: 'Foo'


####################################################################################
# lists
####################################################################################

# - Changeable
# - Ordered. Can be done index operations
# - İnclusiveness

notes = [1, 2, 3, 4]
type(notes)

names = ['a', 'b', 'c', 'd']

not_nam = [1, 2, 3, 'a', 'b', True, [1, 2, 3]]

not_nam[0]
not_nam[5]

not_nam[6] # output: [1, 2, 3]
type(not_nam[6]) # output: list

not_nam[6][2] # output: 3
type(not_nam[6][2]) # output: int

not_nam[1] = 11
print(not_nam[1])

not_nam[:4] # output: [1, 2, 3, 'a']

# List methods
dir(notes)

# append
# clear
# copy
# count
# extend
# index
# insert
# pop
# remove
# reverse
# sort

# Len method
len(notes) # 4
len(not_nam) # 7

# Append method
notes.append(100) # [1, 2, 3, 4, 100]

# Pop method
notes.pop(0) # [2, 3, 4, 100]

# Insert method 
notes.insert(4, "last") # [2, 3, 4, 100, 'last']
notes.insert(2, 99) # [2, 3, 99, 4, 100, 'last']


####################################################################################
# Dictionary
####################################################################################

# - Changeable
# - Not ordered (til version 3.7)
# - Inclusive

# Key-Value
dictionary = {
    "REG": "Regression",
    "LOG": "Logistic Regression",
    "CART": "Classification and Regression"
}

dictionary["REG"] # output: 'Regression'

dictionary = {
    "REG": ["RMSE", 10],
    "LOG": ["MSE", 20],
    "CART": ["SSE", 30]
}

dictionary["REG"][0]

dictionary = {
    "REG": 10,
    "LOG": 20,
    "CART": 30
}
print(type(dictionary))

dictionary["LOG"]

"REG" in dictionary # output: True
"YSA" in dictionary # output: False

dictionary.get("REG") # ['RMSE', 10]
dictionary.get("LOG")[1] # 20

# Change the value
dictionary["REG"] = ["YSA", 10]
# {'REG': ['YSA', 10], 'LOG': ['MSE', 20], 'CART': ['SSE', 30]}


dir(dict)
# 'clear',
# 'copy',
# 'fromkeys',
# 'get',
# 'items',
# 'keys',
# 'pop',
# 'popitem',
# 'setdefault',
# 'update',
# 'values'


# Take all keys
dictionary.keys()

# Take all values
dictionary.values()

#  Take all items
dictionary.items()
# [('REG', ['YSA', 10]), ('LOG', ['MSE', 20]), ('CART', ['SSE', 30])]

# Updating Key-Value values using update

dictionary.update({"REG": 111}) # Existing key
dictionary.update({"ALM": [77, 29]}) # New key


####################################################################################
# Tuples
####################################################################################
# - Immutable
# - Ordered
# - Comprehensive := Can hold more than one type

t = ("john", "marj", 1, 2)
type(t)

# With its ordered functionality we can access of its members like that:
print(t[0] + " " + t[1])
print(t[2:4])

# t[0] = "changed" # Result is "TypeError"

# ANOTHER WAY for changing:

t = list(t)

t[0] = "changed"
t = tuple(t)
print(t)


####################################################################################
# Set
####################################################################################
# - Mutable
# - Unordered + Unchangeable (or unique)
# - Comprehensive (can hold any type data in one variable)
# - Duplicates not allowed


# Difference between different sets
# using : difference()

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

# Ones that are in set1 and aren't in set2
set1.difference(set2)
# also
set_diff1 = set1 - set2
print(set_diff1)

# Ones that are in set2 and aren't in set1
set2.difference(set1)
# also
set_diff2 = set2 - set1
print(set_diff2)


# symmetric_difference() := values that aren't in them one another
result1 = set1.symmetric_difference(set2)
result2 = set2.symmetric_difference(set1)
print(
    result2 == result1, "\n", result1 if result1 == result2 else "null"
)

# also
result3 = set([])

for element in (set_diff1 | set_diff2):
    result3.add(element)

print("result3 is", result3)
print(result3)


# intersection() := which values are the same in both sets
intersect1 = set1.intersection(set2)
intersect2 = set2.intersection(set1)
print(intersect1 == intersect2, "\n", intersect1 if intersect1 == intersect2 else "null")

# union() := union of all elements in both sets
set1.union(set2)
set2.union(set1)

print(
    " or set1.intersection(set2) == set2", "\n", set1.union(set2) if set1.union(set2) == set2.union(set1) else "they are not the same"
)


# isdisjoint() := Do Both sets doesn't have common elements, or not
print(set1.isdisjoint(set2))
print(set2.isdisjoint(set1))

# issubset() := the set is subset of another one
print(set1.issubset(set2))
print(set2.issubset(set1))

# Exemplifying on another sets
set4_1 = set([1, 2, 3, 5, 7, 9])
set4_2 = set([3, 5, 9])

print(set4_1.issubset(set4_2)) # (result) False
print(set4_2.issubset(set4_1)) # (result) True

# issuperset()
print(set4_1.issuperset(set4_2)) # (result) True
print(set4_2.issuperset(set4_1)) # (result) False

