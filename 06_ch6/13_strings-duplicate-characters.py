string1 = input('Enter a string: ')
string2 = set(string1)

if len(string1) == len(string2):
    print('No duplicates')
else:
    print('Contains duplicate(s)')