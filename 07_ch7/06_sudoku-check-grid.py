def main(grid_ok):
    sudoku_1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    sudoku_2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]
    print(grid_ok(sudoku_1))
    print(grid_ok(sudoku_2))

def row_ok(sudoku, row_index):
    current_row = sudoku[row_index]
    test = []

    for num in current_row:
        if num != 0:
            test.append(num)
    
    if len(test) == len(set(test)):
        return True
    else:
        return False

def column_ok(sudoku, column_index):
    test = []

    for row in sudoku:
        if row[column_index] != 0:
            test.append(row[column_index])
    
    if len(test) == len(set(test)):
        return True
    else:
        return False
    
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

def grid_ok(grid):

    for i in range(9):
        if not row_ok(grid, i) and column_ok(grid, i):
            return False
    
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if not block_ok(grid, row, col):
                return False
            
    return True

if __name__ == '__main__':
    main(grid_ok)
        
        


