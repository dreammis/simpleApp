def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a ,b = b,a+b
        n = n+1





def triangles():
    a = [1]
    n = 1
    while n<10:
        yield a
        if n<2:
            a = [1, 1]
            n = n +1
        else:
            a = a[:1] + [a[i]+a[i+1] for i in range(len(a)) if i != len(a)-1] + a[-1:]
            n = n+1



# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break

from datetime import datetime


# def log(func):
#     def wrapper(*args,**kwargs):
#         print 'call %s()'% func.__name__
#         return func(*args,**kwargs)
#     return wrapper()

def log(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper

def loge(text):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print ('%s call %s():'%(text,func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return decorator

@loge('me')
def now():
    print ('2015-3-25')


now()






def rabbitfib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return b



l1 = [1, 2, 4, 7,  9, 34]

l2 = [5, 8, 11, 22,  24, 34]


def merge_two_ordered_list(list1, list2):
    new_list = []

    while len(list1) >0 and len(list2)>0:
        if list1[0] > list2[0]:
            new_list.append(list1[0])
            del(list1[0])
        else:
            new_list.append(list2[0])
            del(list2[0])
    return new_list

merge_two_ordered_list(l1, l2)








