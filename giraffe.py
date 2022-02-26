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

# is_male = False
# is_tall = True

# if is_male or is_tall:
#     print("Please use the gents, Mr. tola?")
# else:
#     print("Please use the ladies, Ms. Petty")

# if is_male and is_tall:
#     print("Hi Boss")
# else:
#     print("Hello Madam!")

# if is_male and is_tall:
#     print("Hi Boss")
# elif is_male and not(is_tall):
#     print("Hi Little Man")
# elif not(is_male) and is_tall:
#     print("Hi Cutie")
# else:
#     print("Hello Madam!")


# comparism operators
# comparism involving other data typesaside booleans only

# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3


# print(max_num(69, 524, 302))


# Calculator App

num1 = float(input('Enter the first number: '))
operator = input('Enter operator: ')
num2 = float(input('Enter the second number: '))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '/':
    print(num1 / num2)
elif operator == '*':
    print(num1 * num2)
else:
    print('invalid operator!')
