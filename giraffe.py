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

# num1 = float(input('Enter the first number: '))
# operator = input('Enter operator: ')
# num2 = float(input('Enter the second number: '))

# if operator == '+':
#     print(num1 + num2)
# elif operator == '-':
#     print(num1 - num2)
# elif operator == '/':
#     print(num1 / num2)
# elif operator == '*':
#     print(num1 * num2)
# else:
#     print('invalid operator!')


# Dictionary
# month_conversions = {
#     'Jan': 'January',
#     'Feb': 'February',
#     'Mar': 'March',
#     'Apr': 'April',
#     'May': 'May',
#     'Jun': 'June',
#     'Jul': 'July',
#     'Aug': 'August',
#     'Sep': 'September',
#     'Oct': 'October',
#     'Nov': 'November',
#     'Dec': 'December',
# }

# print(month_conversions['Apr'])
# print(month_conversions.get('Feb'))


# Do while
# i = 1
# while i < 10:
#     print('my number is ' + str(i))
#     i += 1

# print('my number is finished')

# Guessing Game
# secret_word = 'giraffe'
# guess = ''
# guess_count = 0
# guess_limit = 5
# out_of_guesses = False


# while secret_word != guess and not (out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input('Enter guess: ')
#         guess_count += 1
#     else:
#         out_of_guesses = True

# if out_of_guesses:
#     print('Out of guesses, YOU LOSE!')
# else:
#     print('Yatar! You Won!')

# for loops
# for letter in 'Giraffe Academy':
#     print(letter)
friends = ['Ronaldo', 'Kante', 'Tuchel']
for friend in friends:
    print(friend)
