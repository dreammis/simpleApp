import asyncio
loop = asyncio.get_event_loop()

# @asyncio.coroutine
# def hello():
#     print('hello')
#     yield from asyncio.sleep(3)
#     print('world!')
@asyncio.coroutine
def hello():
    print('hello')
    yield from asyncio.sleep(2)
    print('world!')


if __name__ == '__main__':
    loop.run_until_complete(hello())
    # for i in range(10):
    #     loop.run_until_complete()
    #     loop.run_until_complete(hello())
    # map(loop.run_until_complete(hello()), range(10))
