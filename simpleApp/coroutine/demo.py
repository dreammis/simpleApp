import random


def square():
    while True:
        value = yield
        print(value * value)


def minimize(l=[]):
    while True:
        value = yield
        l.append(value)
        print("now list: " + str(l))
        print(min(l))


def do_square():
    c = square()
    next(c)
    for i in range(9):
        c.send(i)
    c.close()


# do_square()
c = minimize()
next(c)
i = 0
while i != 10:
    c.send(random.randint(1, 1000))
    i += 1
c.close()
