def oddeven_sort(l):
    '''
    :param List: an unsorted List
    :return:sorted List by oddeven_sort
    :url:https://zh.wikipedia.org/wiki/%E5%A5%87%E5%81%B6%E6%8E%92%E5%BA%8F
    :Average case performance:Theta(n^2)
    '''
    odd_range = range(0,len(l)-1,2)
    even_range = range(1,len(l)-1,2)
    sorted  = True
    while sorted:
        sorted = False
        for i in odd_range:
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1],l[i]
                sorted  = True
        for j in even_range:
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                sorted  = True

List = [12,235,325,32,1,23,123,532,234,23,13,5]
oddeven_sort(List)
print List
