def main():
    x = int(input("Enter an integer: "))
    p2, p3 = pow_2_3(x)
    print(p2)
    print(p3)

def pow_2_3(num):
    p2 = num ** 2
    p3 = num ** 3

    return p2, p3

if __name__ == "__main__":
    main()