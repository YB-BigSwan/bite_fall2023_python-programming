num = int(input('Enter an integer: '))
sum = 0

for i in range(num):
        print(num-i, end = ' ')
        sum += num-i

if sum > 0:
    print(f'\nThe sum is {sum}')
else:
    print('Nothing to be printed')