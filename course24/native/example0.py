import asyncio


async def new_sleep():
    await asyncio.sleep(2)


class Waiting:
    def __await__(self):
        print('Waiting')
        awaitable_object = new_sleep().__await__()
        print('Done with waiting')  # nothing happens. why?

        return awaitable_object


async def main():
    print('Started main()')
    await Waiting()
    print('Finished main()')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
