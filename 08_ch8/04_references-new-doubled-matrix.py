from copy import deepcopy

def main(new_doubled_matrix):
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = new_doubled_matrix(m1)
    print(m1)
    print(m2)

def new_doubled_matrix(m):
    new_m = deepcopy(m)

    for row in range(len(new_m)):
        for col in range(len(new_m[row])):
            new_m[row][col] *= 2
    
    return new_m

main(new_doubled_matrix)