import asyncio


async def hello(name, timeout):
    cnt = 0

    while True and cnt < 2:
        await asyncio.sleep(timeout)
        print('Hello, {}'.format(name))
        cnt += 1

tasks = [
    hello('people', 1),
    hello('friends', 0.5),
    hello('neighbours', 0.3),
]


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
