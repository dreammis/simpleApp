#-* coding:utf8 -*-
from itertools import count,islice,cycle,repeat

"""itertools"""
def itcount():
    """
    count(初值=0, 步长=1)
    count 迭代器会返回从传入的起始参数开始的均匀间隔的数值。count 也可以接收指定的步长参数。
    无限的迭代器之一
    """

    for i in count(10):
        if i>20:
            break
        else:
            print i

def itislice():
    """
    无限的迭代器之一
    配合count可以达到停止迭代的作用,具体在生产环境中如何用还待思考
    """
    for i in islice(count(0),100):
        print i
def itcycle():
    """
    无限迭代器的一种
    """
    for item in cycle("ABC"):
        break
        print item

    tmpdata= ['hello','malgebide','wocao']
    iteror = cycle(tmpdata)
    # 无限循环
    next(iteror)

def itrepeat():
    """
    repeat(对象[, 次数])
    """
    enumerate
    for i in enumerate(repeat(1,20)):
        print i



"""
------------
"""
"""可终止的迭代器"""
from itertools import accumulate,chain,compress,dropwhile
import operator
def itaccumulate():
    """
    accumulate(可迭代对象[, 函数])  
    attention: python3 avaliable!  
    """
    list(accumulate(range(10)))
    # 叠加相加,默认是加,可以自己定义符号
    # [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]

    list(accumulate(range(1,5),operator.mul))
    # 1×1=1, 1×2=2, 2×3=6

def itchain():
    """
    将多个迭代对象中的元素合并
    """
    chain([1,2,3,4],["s","b"])
    # [1,2,3,4,"s","b"]
    # maybe [1,2,3,4]+["s","b"] chain 更为优雅，也更容易理解
    
    #chain.from_iterable(可迭代对象)
    numbers = list(range(5))
    cmd = ['ls', '/some/dir']
    list(chain.from_iterable([cmd, numbers]))

def itcompress():
    """
    compress(数据, 选择器)
    para 1:data
    para 2:bools
    """
    letters = 'abcd'
    bools = [True, False, True, True]
    list(compress(letters,bools))
    # [a,c,d]

"""
dropwhile(断言, 可迭代对象)
list(dropwhile(lambda x:x<5,[1,4,6,4,1]))
[6,4,1]
使用lambda循环便利可迭代对象
一旦返回False,将后面的输出出来
如上面例子,一旦发现大于等于5的值出现其他的全部保留

filterfalse  python3 avaliable..
如果整数值大于等于 5，这个整数将保留下来，否则将被舍弃
from itertools import filterfalse
def greater_than_five(x):
     return x > 5 

两者区别
list(filterfalse(greater_than_five, [6, 7, 8, 9, 1, 2, 3, 10]))
[1, 2, 3]
list(dropwhile(greater_than_five, [6, 7, 8, 9, 1, 2, 3, 10]))
[1, 2, 3, 10]
"""

if __name__=='__main__':
    itrepeat()