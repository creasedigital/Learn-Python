friends = ['Kelvin', 'Jim', 'Karen', 'Jim', 'Champion', 'Jim', 'Drury']
lucky_numbers = [8, 4, 42, 7, 5]

# friends.extend(lucky_numbers)
friends.append('Ronaldo')  # adds last element to the list

# adds quoted element to the specified list position
friends.insert(0, 'Shelvey')

friends.pop()  # removes last element from the list

print(friends)

print(friends.count('Jim'))  # counts the number of that item found in the list

friends.reverse()  # reverse the list

friends.sort()  # sort the list alphabetically


print(friends.index('Drury'))

friends2 = friends.copy()

print(friends)
print(friends2)

# print(friends[2])

# print('My commentators are: Jon ' +
#       friends[3] + ' and ' + friends[2] + ' Beglin')

# print(friends[1:])
# print(friends[1:2])
# print(friends[1:-1])
