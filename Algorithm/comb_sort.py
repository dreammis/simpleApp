#-* coding:utf8 -*-

def comb_sort(List):
    '''
    :param List: an unsorted List
    :return:sorted List by comb_sort
    :url:https://zh.wikipedia.org/wiki/%E6%A2%B3%E6%8E%92%E5%BA%8F
    :Average case performance:Omega (n^{2}/2^{p})
    '''
    dis = int(len(List)/1.3)
    while dis:
        for i in range(len(List)-dis):
            if List[i]>List[i+dis]:List[i],List[i+dis]=List[i+dis],List[i]
        dis = int(dis/1.3)




List = [12,235,325,32,1,23,123,532,234,23,13,5]

# comb_sort(List)
# print List





