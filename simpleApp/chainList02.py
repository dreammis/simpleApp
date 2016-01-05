'''
Making a flat list out of list of lists in Python (advance)
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



li=[1,[2],[[3]],[[4,[5],6]]]

def func01(li):
    new = []
    for item in li:
        if isinstance(item,list):
            new.extend(func01(item))
        else:
            new.append(item)
    return new

def func02(li):
    s = str(li).replace('[','').replace(']','')
    return [eval(i.strip()) for i in s.split(',')]


