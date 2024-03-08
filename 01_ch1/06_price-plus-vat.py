try:
    price = float(input('Enter price: '))
    vat = 0.24
    totalPrice = (price * vat) + price
    print(f'The price with VAT is {totalPrice:.2f}')
except ValueError:
    print('Invalid price')