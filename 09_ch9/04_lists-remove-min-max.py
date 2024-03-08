def main(remove_min_max):
    a = [3, 1, 4, 1, 5]
    remove_min_max(a)
    print(a)

def remove_min_max(list):
    
    if len(list) > 0:
        list.sort()
        del list[0]
        if len(list) > 0:
            del list[len(list) -1]
            


if __name__ == "__main__":
    main(remove_min_max)