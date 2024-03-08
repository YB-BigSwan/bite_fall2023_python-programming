def compute_earnings(wage, hours):
    if hours > 40:
        overtime = hours - 40
        total_earnings = (wage * 40) + ((wage * 1.5) * overtime)
        return total_earnings
    else: 
        total_earnings = wage * hours
        return total_earnings


def main():
    wage = float(input('Enter wage: '))
    hours = int(input('Enter hours: '))
    total_earnings = compute_earnings(wage, hours)
    print(f'The earnings are {total_earnings:.2f}')

main()