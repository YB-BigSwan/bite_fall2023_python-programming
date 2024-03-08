check = False

while check == False:  
    monthNumber = input('Enter a month number: ')

    try:
        monthNumber = int(monthNumber)

        if 0 < monthNumber < 13:
           print('OK') 
           check = True
        else:
           print(f'{monthNumber} is not a valid month number\n') 

    except ValueError:
        print(f'\'{monthNumber}\' is not a valid month number\n')