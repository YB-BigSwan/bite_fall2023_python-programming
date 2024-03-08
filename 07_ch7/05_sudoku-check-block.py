def main(block_ok):
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 6],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(block_ok(sudoku, row_index=0, column_index=0))
    print(block_ok(sudoku, row_index=3, column_index=6))
    print(block_ok(sudoku, row_index=6, column_index=3)) 

def block_ok(sudoku, row_index, column_index):
    test = []

    if row_index % 3 != 0 or column_index % 3 != 0:
        return False

    for row in range(row_index, row_index +3):
        for col in range(column_index, column_index + 3):
            num = sudoku[row][col]
            if num != 0:
                test.append(num)
        
    if len(test) == len(set(test)):
        return True
    else:
        return False
    
if __name__ == '__main__':
    main(block_ok)