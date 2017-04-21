# -*- coding: utf-8 -*-

import async_timeout
import asyncio

import aiohttp
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()


async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        urls = [
            'http://python.org',
            'http://ya.ru',
            'http://habrahabr.ru',
        ]
        for url in urls:
            html = await fetch(session, url)
            print(url, html)


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
