for lucky_number in range(1, 21):
    if (lucky_number == 4 or lucky_number == 13):
        print(f'{lucky_number}, you are the chosen one')
    elif (lucky_number % 2) == 0:
        print(f'{lucky_number}, is even')
    elif (lucky_number % 2) == 1:
        print(f'{lucky_number}, is odd')
    else:
        print('thanks for trying')
