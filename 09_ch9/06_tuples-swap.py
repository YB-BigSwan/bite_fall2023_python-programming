def main():
    list = []

    for i in range(7):
        num = int(input('Enter an integer: '))
        list.append(num)

    for i in range(0, 6, 2):
        list[i], list[i + 1] = list[i + 1], list[i]

    print(list)
    
main()

    
