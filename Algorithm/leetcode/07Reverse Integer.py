'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
'''


class Solution(object):
    def reverse(self, x):
        judge = cmp(x, 0)
        abss = int(`judge * x`[::-1])
        return abss * judge * (abss < 2 ** 31)
