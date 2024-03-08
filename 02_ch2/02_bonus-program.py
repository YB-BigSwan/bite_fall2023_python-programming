price = int(input("Enter the car's selling price: "))

if price < 50000:
    bonus = price * 0.01
else:
    bonus = price * 0.015

bonus = max(200, bonus)

print(f'The bonus is {bonus:.2f} euros.')
