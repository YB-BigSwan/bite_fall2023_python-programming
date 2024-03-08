def is_prime(number):
    if number <= 1:
        return False
    if 1 < number <= 3:
        return True
    
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    

def is_circular_prime(number):
    if is_prime(number) == False:
        return False
    number_to_string = str(number)
    for i in range(len(number_to_string)):
        if is_prime(int(number_to_string)) == False:
            return False
        number_to_string = number_to_string[1:] + number_to_string[0]
    return True
    
    

def main():
    number = int(input('Enter a positive integer: '))

    if is_circular_prime(number) == True:
        print(f'{number} is a circular prime')
    else:
        print(f'{number} is not a circular prime')

if __name__ == '__main__':
    main()