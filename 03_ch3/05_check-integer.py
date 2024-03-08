num = input('Enter an integer: ')

try:
    int(num)
    print('OK')
except ValueError:
    print(f'\'{num}\' is not an integer')