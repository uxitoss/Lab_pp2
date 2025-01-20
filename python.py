#HOME, Intro, Getting Started
print("Hello, World!")

#Syntax
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

#Comments
#This is a comment
print("Hello, World!")


#Variables
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Output Variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Data Types
'''
Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
None Type: NoneType
'''

x = 5
print(type(x))

#Numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#Strings
print("Hello")
print('Hello')

#Slicing Strings
b = "Hello, World!"
print(b[2:5])

#Modify Strings
a = "Hello, World!"
print(a.upper())

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#String Format
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Escape Character
txt = "We are the so-called \"Vikings\" from the north."