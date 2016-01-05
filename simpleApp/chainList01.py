'''
Making a flat list out of list of lists in Python
'''
import time
import itertools

def time_cost(func):
    def deco(*args,**kwargs):
        start = time.clock()
        result = func(*args,**kwargs)
        print ('the function %s costs %fs long.')%(func.__name__,time.clock()-start)
        return result
    return deco

@time_cost
def func01(li):
    '''
    use the list analysis
    :param li:
    :return:
    '''
    result = [item for subList in li for item in subList]
    return result

@time_cost
def func02(li):
    '''
    ues the itertools -chain
    :param li:
    :return:
    '''
    result = list(itertools.chain(*li))
    return result

@time_cost
def func03(li):
    '''
    ues the reduce
    :param li:
    :return:
    '''
    result = reduce(lambda x,y:x+y,li)
    return result

l = [[1,2,3],[4,5,6], [7], [8,9]]*101

@time_cost
def func04(li):
    '''
    ues the itertools -chain-from_iterable
    :param li:
    :return:
    '''
    result = list(itertools.chain.from_iterable(li))
    return result

func01(l)
func02(l)
func03(l)
func04(l)
