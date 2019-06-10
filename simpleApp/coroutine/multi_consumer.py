def producer(consumers):
    print("producer is Ready!")
    try:
        while True:
            val = yield
            for consumer in consumers:
                consumer.send(val * val)
    except GeneratorExit:
        for consumer in consumers:
            consumer.close()


def consumer(name, low, high):
    print("consumer is Ready!")
    try:
        while True:
            val = yield
            if low < val < high:
                print("%s got " % name, val)
    except GeneratorExit:
        print("%s closed" % name)


con1 = consumer("Consumer 1", 0, 10)
con2 = consumer("Consumer 2", 10, 20)
con3 = consumer("Consumer 3", 20, 30)
cs = [con1, con2, con3]
pro = producer(cs)

next(pro)

for c in cs:
    next(c)

pro.send(2)
pro.send(4)
pro.send(3)

pro.send(5)

pro.close()
