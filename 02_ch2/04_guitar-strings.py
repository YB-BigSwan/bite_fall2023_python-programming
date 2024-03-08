gigNumber = float(input('Number of gigs: '))
gigPerString = float(input('Gigs to be played with the same set of strings: '))
pricePerString = float(input('Price of a set of guitar strings: '))

stringsNeeded = gigNumber//gigPerString
if (gigNumber%gigPerString) > 0:
    stringsNeeded = stringsNeeded + 1

price = stringsNeeded * pricePerString

print(f'\nThe guitarist needs {stringsNeeded:.0f} new sets of guitar strings')
print(f'The total cost is {price:.2f} euros')