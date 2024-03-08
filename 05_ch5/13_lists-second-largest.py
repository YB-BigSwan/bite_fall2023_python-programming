def second_largest(list):
    if len(list) < 2:
        return None
    
    sorted_list = sorted(set(list))
    sorted_list.remove(max(sorted_list))

    return(max(sorted_list))


    

    

