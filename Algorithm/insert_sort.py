def insert_sort(List):
    sorted = 1
    while sorted == len(List):



        for i in range(sorted,0,-1):
            if List[i]>


        sorted +=1


def insert_sort(l):
    print l
    for i in range(1,len(l)): #从第二个元素开始
        value = l[i]
        while i >= 1 and l[i-1] > value:
            l[i] = l[i-1]
            i -= 1
        l[i] = value
    return l
l = [8, 4, 3, 1, 6, 9, 2, 7]
print insert_sort(l)



    # mark first element as sorted
    # for each unsorted element
    #   'extract' the element
    #   for i = lastSortedIndex to 0
    #     if currentSortedElement > extractedElement
    #       move sorted element to the right by 1
    #     else: insert extracted element