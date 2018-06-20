class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, lookup = [], {'(': ')', '{': '}', '[': ']'}
        for value in s:
            if value in lookup:
                stack.append(value)
            elif lookup.get(value) is None or len(stack)==0 or lookup[value] != stack.pop():
                return False
        return len(stack) == 0
