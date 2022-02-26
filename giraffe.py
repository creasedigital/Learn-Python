# functions
# -- A collction of codes that performs specific task--

# user = input('Type your name: ')


# def say_hi():
#     print("hello " + user)


# say_hi()


# return statement
# def cube(num):
#     return num**3


# print(cube(3))
# print(cube(4))
# print(cube(6))

# if statement (conditionals) helps make our program smarter

is_male = False
is_tall = True

if is_male or is_tall:
    print("Please use the gents, Mr. tola?")
else:
    print("Please use the ladies, Ms. Petty")

if is_male and is_tall:
    print("Hi Boss")
else:
    print("Hello Madam!")

if is_male and is_tall:
    print("Hi Boss")
elif is_male and not(is_tall):
    print("Hi Little Man")
elif not(is_male) and is_tall:
    print("Hi Cutie")
else:
    print("Hello Madam!")
