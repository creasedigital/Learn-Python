try:
    nums = int(input('How many times do I have to tell you?\n'))

    if type(nums) == int:
        for num in range(nums):
            print('CLEAN UP YOUR ROOM!')
except:
    print('enter a valid digit')
