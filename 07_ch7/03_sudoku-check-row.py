def main(row_ok):
    sudoku = [
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
    print(row_ok(sudoku, row_index=0))
    print(row_ok(sudoku, row_index=1)) 
    print(row_ok(sudoku, row_index=8)) 

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
    
if __name__ == '__main__':
    main(row_ok)



