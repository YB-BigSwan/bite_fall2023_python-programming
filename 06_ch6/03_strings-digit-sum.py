string = input('Enter a string: ')
nums = []

for i in string:
    if i.isdigit():
        nums.append(int(i))

if len(nums) > 0:
    print(f'\nThe sum of digits is {sum(nums)}')
else:
    print('\nThe sum of digits is 0')