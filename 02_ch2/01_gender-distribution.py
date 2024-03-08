female = int(input('Enter the number of female students: '))
male = int(input('Enter the number of male students: '))

total = female + male

if total == 0:
    print(f'\nFemale: {0:.1f} %')
    print(f'Male: {0:.1f} %')
else:
    print(f'\nFemale: {((female / total) * 100):.1f} %')
    print(f'Male: {((male / total) * 100):.1f} %')