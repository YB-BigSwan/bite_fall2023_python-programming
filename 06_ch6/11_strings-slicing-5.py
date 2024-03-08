string = input('Enter a string: ')
character = input('Enter a character: ')

for i in range(len(string) - 3):
    if string[i] == character:
        print(string[i:i + 4])