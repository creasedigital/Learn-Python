# -------------------------------------COMMENTS
# This is a single line comment

# Below is a multi-line comment
'''print('Hello, world!')
print(1 + 2)
trying out python
'''
# Below is a single line comment also
# "print('Hello\n Python')"

# Here is how we print to our console
# print('Python is \n awesome')

# -------------------------------------DATA TYPES
# Data Types type() command is used to check a data type
'''
The Computer needs to know
the kind of data you want it
to process
'''
# strings - are represented with any character inside single or double quotes e.g. 'John'
# int - also known as integers are represented with whole numbers value e.g. 546892
# float -  are represented with decimal numbers value e.g. 63.52
# bool - booleans are represented with a True or False value


print(type('John'))
print(type(546892))
print(type(63.52))
print(type(False))

# ----------------------------------------VARIABLES
# Naming conventions used in python includes:
'''The use of underscore to connect values rather than space'''
# variables are use to store values to make them reusable

user_age = 50
user_location = 'Abuja'
user_height = 186

# variable reassignment
user_age = 30

# commas are used to declare multiple values in a function
print(user_age, user_location, user_height)
