def remove_successive_duplicates(list):
    new_list = []
    num = None
    for i in range(len(list)):
        if list[i] != num:
            new_list.append(list[i])
            num = list[i]
            
    list.clear()
    list.extend(new_list)


            
        