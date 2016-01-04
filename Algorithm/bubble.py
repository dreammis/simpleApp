#-* coding:utf8 -*-

def bubble(List):
    '''
    :param List: an unsorted List
    :return:sorted List by bubble
    :url:https://zh.wikipedia.org/wiki/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F
    :Average case performance:O(n^2)
    '''
    for i in range(len(List)-1,0,-1):
        for j in range(i):
            if List[j]>List[j+1]:List[j],List[j+1]=List[j+1],List[j]



List = [12,235,325,32,1,23,123,532,234,23,13,5]

bubble(List)
print List
