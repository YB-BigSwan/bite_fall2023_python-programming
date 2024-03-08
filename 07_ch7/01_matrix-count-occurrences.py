def main(count_occurrences):
    m = [[1, 2, 3], [1, 2, 2], [1, 1, 1], [1, 2, 1]]
    print(count_occurrences(m, 1))
    print(count_occurrences(m, 2))
    print(count_occurrences(m, 5))

def count_occurrences(m, input):
    count = 0
    for row in m:
        for num in row:
            if num == input:
                count += 1
    return count

if __name__ == '__main__':
    main(count_occurrences)