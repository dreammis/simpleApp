# coding: utf-8

__metaclass__ = type
class Bird:
    def __init__(self):
        print 'father'
        self.cansing = True
    def eat(self):
        print 'i can eat'

    def sing(self):
        if self.cansing:
            print 'i can sing'

class Sparrow(Bird):
    def __init__(self):
        super(Sparrow,self).__init__()
        print 're-father'

    def jump(self):
        print 'i can jump'

S = Sparrow()
S.jump()
S.eat()
S.sing()