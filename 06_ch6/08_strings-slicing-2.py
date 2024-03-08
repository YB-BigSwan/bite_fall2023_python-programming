string = input('Enter a string: ')
if len(string) < 2:
    print('Too short string')
else:
    print(string[len(string) - 2])