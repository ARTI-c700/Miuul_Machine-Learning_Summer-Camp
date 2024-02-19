
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

dictionary  = {
    "REG": 10,
    "LOG": 20,
    "CART": 30
}

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
