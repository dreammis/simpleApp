#-* coding:utf8 -*-
'''
计算字符串中单词出现的频率
'''


class counter():
    def __init__(self):
        self.dict = {}

    def add(self,word):
        count = self.dict.setdefault(word,0)
        self.dict[word] = count+1

    def count(self,desc=None):
        result = [[val, key] for (key, val) in self.dict.items()]
        result.sort()
        if desc:
            result.reverse()
        return result

if __name__ == "__main__":
    a = '''
    I was confused by the copysign documentation and thought the parameter had to be a float. However, integers work (I just tested it) so there's no need for the cast. I've edited the answer.
        '''
    c = counter()
    words = a.split()
    for word in words:
        c.add(word)
    print c.count()