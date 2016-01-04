#-* coding:utf8 -*-

def deco(func):
	'''
	对参数数量不确定的函数进行装饰
	'''
	def _deco(*args,**kwargs):
		print ("before the function %s called."%func.__name__)

		ret = func(*args,**kwargs)

		print ("after the function %s called the result:%s"%(func.__name__,ret))
	return _deco

@deco
def plus(a,b):
	print ("plus(%s,%s) called."%(a,b))
	return a*b
@deco
def third(a,b,c):
	print ("third called.")
	return c*b*a


plus(10,5)

third(2,534,534)



#使用装饰器带参数

def deco(args):
	def _deco(func):
		def __deco():
			print ("print %s called [%s]."%(func.__name__,args))

			func()

			print ("after %s called [%s]."%(func.__name__,args))
		return __deco
	return _deco


@deco("myfunction")
def function():
	print ("function called.")

function()



import time
import functools
 
def timeit(func):
    @functools.wraps(func)
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print 'used:', end - start
    return wrapper
 
@timeit
def foo():
    print 'in foo()'
 
foo()
print foo.__name__