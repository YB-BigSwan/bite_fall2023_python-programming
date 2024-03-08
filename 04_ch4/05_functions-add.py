def add(num1, num2):
    fix_round = num1 + num2 + 0.001
    total = round(fix_round)
    return total


def main():
    num1 = float(input('Enter a float: '))
    num2 = float(input('Enter a float: '))
    total = add(num1, num2)
    print(total)

main()
