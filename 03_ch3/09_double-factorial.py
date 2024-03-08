number = int(input("Enter a non-negative integer: "))

if number < 0:
    print('Please enter a non-negative integer')
else:
    multiplicand = 1

    for i in range(number, 0, -2):
        multiplicand = multiplicand * i

print(f'{number}!! = {multiplicand}')