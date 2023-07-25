##########################################
# İntroduction & Quick recap
##########################################

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
x = ["name": "Peter", "Age": 36]

# Tuple
x = ("python", "ml", "ds")
type(x) # Output : tuple

# Sets
x = {"python", "ml", "ds"}
type(x) # Output : set

# Note: Lists, Tuples and Dictionary data structures are also called "Python Collections" 


##########################################
# Numbers
##########################################
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


##########################################
# Strings
##########################################
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


##########################################
# String methods
##########################################
# identify methods that belong to a specific ds
dir(int)
