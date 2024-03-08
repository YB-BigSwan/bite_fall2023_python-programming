intRate = float(input('Enter interest rate: '))
tax = float(input('Enter capital income tax rate: '))
deposit = float(input('Enter initial deposit: '))
years = int(input('Enter number of years: '))

intRate = intRate / 100
tax = tax / 100

balance = deposit

print()
for i in range(years):
    interest = balance * intRate
    afterTax = interest * (1 - tax)
    balance += afterTax
    print(f'Year {i + 1}: {balance:.2f}')