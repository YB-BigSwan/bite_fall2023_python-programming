from datetime import date
from calendar import monthrange

def print_month_calendar(year, month):
    month_names = ["", "January", "February", "March", "April", "May","June",
    "July", "August", "September", "October", "November", "December"]
    day_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    my_date = date(year, month, 1)
    days_in_month = monthrange(my_date.year, my_date.month)[1]
    day_of_week = my_date.weekday() + 1

    print(f'\n > {month_names[month]} {year} <')

    for dow in range(7):
        print(f' {day_names[dow]}', end = '')
    
    print()

    for i in range(day_of_week - 1):
        print('    ', end = '')

    for day in range(1, days_in_month + 1):
        print(f'{day:4}', end = '')

        if (day + day_of_week -1) % 7 == 0:
            print()
        if day == days_in_month and (day + day_of_week - 1) % 7 != 0:
            print()

def main():
    year = int(input('Enter year: '))
    month = int(input('Enter month: '))
    print_month_calendar(year, month)

if __name__ == '__main__':
    main()