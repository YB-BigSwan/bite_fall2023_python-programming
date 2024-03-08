def main(multiply_by_two):
    numbers = [1, 2, 3, 4, 5, 6]
    more_numbers = [10, 20, 30]
    print(numbers)
    multiply_by_two(numbers)
    print(numbers)
    print(more_numbers)
    multiply_by_two(more_numbers)
    print(more_numbers)

def multiply_by_two(number_set):
    for i in range(len(number_set)):
        number_set[i] *= 2

if __name__ == '__main__':
    main(multiply_by_two)