def main(new_doubled_list):
    first_list = [1, 2, 3, 4, 5, 6]
    second_list = new_doubled_list(first_list)
    print(first_list)
    print(second_list)

def new_doubled_list(list):
    new_list = list.copy()

    for i in range(len(new_list)):
        new_list[i] *= 2
    
    return new_list

main(new_doubled_list)