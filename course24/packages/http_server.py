# -*- coding: utf-8 -*-


import asyncio
import uvloop
from aiohttp import web

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = 'Hello, ' + name
    return web.Response(text=text)


app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)

web.run_app(app, host='127.0.0.1', port=8000)
