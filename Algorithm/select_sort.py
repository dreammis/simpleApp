def select_sort(List):
    index = len(List)-1
    while index:
        max_index = index
        for i in range(index):
            if List[i]>List[max_index]:max_index = i
        if List[max_index]>List[index]:List[max_index],List[index] = List[index],List[max_index]
        index -=1