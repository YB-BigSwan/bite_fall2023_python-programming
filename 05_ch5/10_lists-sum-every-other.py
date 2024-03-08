def sum_every_other(num_list):
    if len(num_list) == 0:
        return None
    
    list_sum = 0
        
    for i in range(len(num_list)):
        if (i % 2) == 0:
            list_sum += num_list[i]
    return list_sum