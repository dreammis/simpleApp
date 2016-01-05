#ues the normal way

def normalIn():
    keys = ('name', 'age', 'food')
    values = ('Monty', 42, 'spam')
    d = dict(zip(keys,values))
    return d



def uesItertools():
    import itertools
    keys = ('name', 'age', 'food')
    values = ('Monty', 42, 'spam')
    d = dict(itertools.izip(keys,values))
    return d


def specialC():
    import itertools
    keys = ('name', 'age', 'food','young')
    values = ('Monty', 42, 'spam')
    d = dict(itertools.izip_longest(keys,values))
    return d

'''
l = [[1,2,3],[4,5,6], [7], [8,9]]
change to:
[1, 2, 3, 4, 5, 6, 4, 5, 6, 7, 8, 9]
'''
l = [[1,2,3],[4,5,6], [7], [8,9]]


