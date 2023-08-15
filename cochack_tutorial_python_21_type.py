import random

# Text Type:
# str
# Numeric Types:
# int, float, complex
# Sequence Types:
# list, tuple, range
# Mapping Type:
# dict
# Set Types:
# set, frozenset
# Boolean Type:
# bool
# Binary Types:
# bytes, bytearray,

# getting the data type using the type() function
x = 5
print(type(x))

# x = "Hello World"
# str
# x = 20
# int
# x = 20.5
# float
# x = 1j
# complex
# x = ["apple", "banana", "cherry"]
# list
# x = ("apple", "banana", "cherry")
# tuple
# x = range(6)
# range
# x = {"name" : "John", "age" : 36}
# dict
# x = {"apple", "banana", "cherry"}
# set
# x = frozenset({"apple", "banana", "cherry"})
# frozenset
# x = True
# bool
# x = b"Hello"
# bytes
# x = bytearray(5)
# bytearray
# x = memoryview(bytes(5))
# memoryview

# You could also set the data type using a constructor

# x = str("Hello World")
# str
# x = int(20)
# int
# x = float(20.5)
# float
# x = complex(1j)
# complex
# x = list(("apple", "banana", "cherry"))
# list
# x = tuple(("apple", "banana", "cherry"))
# tuple
# x = range(6)
# range
# x = dict(name="John", age=36)
# dict
# x = set(("apple", "banana", "cherry"))
# set
# x = frozenset(("apple", "banana", "cherry"))
# frozenset
# x = bool(5)
# bool
# x = bytes(5)
# bytes
# x = bytearray(5)
# bytearray
# x = memoryview(bytes(5))
# memoryview

# There are three numeric types in Python:
# int, float and complex
# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# Convert from one type to another:
x = 1 # int
y = 2.8 # float
z = 1j # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

#you cannot convert complex numbers into another number type


print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Type casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'


print(random.randrange(1,10)) 
