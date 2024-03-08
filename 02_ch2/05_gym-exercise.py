daysPerYear = float(input('Enter the number of days of gym visits per year: '))
dayPass = float(input('Enter price for a day pass: '))
yearlyMembership = float(input('Enter yearly membership fee: '))
dayPassCost = dayPass * daysPerYear

if dayPassCost < yearlyMembership:
    print(f'\nBuying day passes is {(yearlyMembership - dayPassCost):.2f} euros cheaper')
elif dayPassCost == yearlyMembership:
    print('\nThere is no price difference')
else:
    print(f'\nPaying the yearly membership fee is {(dayPassCost - yearlyMembership):.2f} euros cheaper')