def double_factorial(i):
    multiplicand = 1
    for j in range(i, 0, -2):
        multiplicand = multiplicand * j
    return multiplicand
    

def main():
    for i in range(10):
        result = double_factorial(i)
        print(f'{i}!! = {result}')

if __name__ == "__main__":
    main()