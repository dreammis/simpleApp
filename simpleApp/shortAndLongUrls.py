# -*- coding:utf-8 -*-
# class A(object):
#     def foo(self,x):
#         print "executing foo(%s,%s)"%(self,x)
#     @classmethod
#     def class_foo(cls,x):
#         print "executing class_foo(%s,%s)"%(cls,x)
#         cls().foo(x)
#     @staticmethod
#     def static_foo(x):
#         print "executing static_foo(%s)"%x
# a=A()
# a.foo(1)
# print '1'
# a.class_foo(1)
# print '2'
# A.class_foo(1)
# print '3'
# a.static_foo(1)
# '''
# executing foo(<__main__.A object at 0x01AA17F0>,1)
# 1
# executing class_foo(,1)
#
# executing foo(<__main__.A object at 0x01AA1830>,1)
# 2
# executing class_foo(,1)
#
# executing foo(<__main__.A object at 0x01AA1830>,1)
# 3
# executing static_foo(1)
# '''


# -*- coding:utf-8 -*-
import urllib2, socket,requests
request = urllib2.urlopen(urllib2.Request(url='http://t.cn/zOyhXrZ', headers = {'User-Agent':'Mozilla/8.0 (compatible; MSIE 8.0; Windows 7)'}))
socket.setdefaulttimeout(5)
print request.url

url = requests.get(url='http://t.cn/zOyhXrZ').url
print url
