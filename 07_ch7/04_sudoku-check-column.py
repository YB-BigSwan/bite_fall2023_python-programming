def main(column_ok):
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
    print(column_ok(sudoku, column_index=0))
    print(column_ok(sudoku, column_index=1))
    print(column_ok(sudoku, column_index=8)) 

def column_ok(sudoku, column_index):
    test = []

    for row in sudoku:
        if row[column_index] != 0:
            test.append(row[column_index])
    
    if len(test) == len(set(test)):
        return True
    else:
        return False
    
if __name__ == '__main__':
    main(column_ok)
