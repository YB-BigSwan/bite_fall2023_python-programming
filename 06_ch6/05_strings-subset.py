string1 = input('Enter first string: ')
string2 = input('Enter second string: ')
count = 0

if len(string2) == 0:
    (print('Nothing to be checked'))

for i in string2:
    if i in string1:
        count += 1

if count == len(string2):
    print('Subset')
else:
    print('Not subset')