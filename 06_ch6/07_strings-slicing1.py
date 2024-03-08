string = input('Enter a string: ')
new_string = ''
print(string[0:2])
for i in range(len(string)):
    if i % 2 == 0:
        new_string += string[i]
print(f'{new_string}')