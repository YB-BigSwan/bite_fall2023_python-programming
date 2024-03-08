weekday = input('Enter a weekday number: ')

try: 
    weekday = int(weekday)
    if 1<= weekday <= 7:
        print('OK')
    else:
        print('Please enter an integer between 1 and 7')

except ValueError:
    print('Please enter an integer between 1 and 7')