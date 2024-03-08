def common_members(list1, list2):
    for i in range(len(list1)):
        if list1[i] in list2:
            return True
        
    return False