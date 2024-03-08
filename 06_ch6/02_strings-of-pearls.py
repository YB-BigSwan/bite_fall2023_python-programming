string = input('Enter first string: ')
count = 0

if string.lower() == 'quit':
    print('\nBye!')

else:
    while string.lower() != 'quit':
        if string.lower() == 'pearl':
            count += 1
        string = input('Enter next string: ')   

    print(f'\n{count} pearls\nBye!')


    