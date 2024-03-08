def compute_discount(price, discount):
    discount_amount = price * ((discount/100))
    return discount_amount
    

def main():
    price = float(input('Enter price: '))
    discount = float(input('Enter discount percentage: '))
    discount_amount = compute_discount(price, discount)
    print(f'The discount is {discount_amount:.2f} euros')
    
main()
