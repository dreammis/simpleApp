from __future__ import division, print_function
from pprint import pprint

keys = 'guido sarah barry rechel tim'.split()
values1 = 'blue orange green yellow red'.split()
values2 = 'austin dallas tuscon reno portlan'.split()
values3 = 'apple banana orange pear peach'.split()

hashes = list(zip(keys, values1, values2, values3))
print(hashes)