def producer(consumer):
    print("producer is Ready!")
    while True:
        val = yield
        consumer.send(val * val)


def consumer():
    print("consumer is Ready!")

    while True:
        val = yield
        print("consumer got the ", val)

c = consumer()
next(c)
p = producer(c)
next(p)

p.send(3)
p.send(6)
p.send(7)
p.close()
c.close()
