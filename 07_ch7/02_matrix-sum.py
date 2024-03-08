def main(print_matrix_sum):
    m1 = [[1, 2, 0], [2, 3, 4]]
    m2 = [[3, 2, 5], [6, 4, 3]]
    m3 = [[1, 1, 1, 1], [3, 3, 2, 1], [2, 2, 2, 2]]
    m4 = [[2, 2, 2, 3], [2, 3, 1, 0], [1, 2, 3, 4]] 
    print_matrix_sum(m1, m2)
    print()
    print_matrix_sum(m3, m4)

def print_matrix_sum(matrix1, matrix2):
    sum = []

    for row in range(len(matrix1)):
        new_row = []
        for col in range(len(matrix1[row])):
            new_row.append(matrix1[row][col] + matrix2[row][col])
        sum.append(new_row)
    
    for row in sum:
        for col in row:
            print(col, end=' ')
        print()


if __name__ == '__main__':
   main(print_matrix_sum)

  