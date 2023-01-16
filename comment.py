"""
a = {'id': 89, 'name': "John"}

print(a.get('age', 0))

for i in [1, 2, 3, 4]:
    print(i, end=" ")

a = {'id': 89, 'name': "John"}
print('age')

for i in range(1, 4):
    print(i, end=" ")

for i in range(0, 3):
    print(i, end=" ")

for i in ["Hello", "Holberton", "School", 98]:
    print(i, end=" ")

a = {'id': 89, 'name': "John"}
print(a.get('age'))
"""


def my_function(counter):
    print("Counter: {}".format(counter))


my_function(12)


def my_function():
    print("In my function")


my_function()


def my_function(counter=89):
    return counter + 1


print(my_function())


def my_function(counter=89):
    print("Counter: {}".format(counter))


my_function()


def my_function():
    print("In my function")

    my_function


def my_function(counter=89):
    print("Counter: {}".format(counter))


my_function(12)

a = [1, 2, 3, 4]
# a.append(5)
print(a[-1])
