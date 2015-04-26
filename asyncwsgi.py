# -*- coding: utf-8 -*-

"""
Async WSGI support for tornado and asyncio
"""

import threading

from functools import wraps
from greenlet import greenlet, getcurrent

local = threading.local()


def coroutine(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not hasattr(local, 'main'):
            raise RuntimeError(
                'Event loop needs to be started with asyncwsgi.run')

        def done(data):
            try:
                assert(data.done())
                gr.switch(data.result())
            except Exception as e:
                gr.throw(e)

        gr = getcurrent()
        gen = local.make_coroutine(f)(*args, **kwargs)
        local.schedule(gen).add_done_callback(done)
        return local.main.switch()

    return wrapper


def wrap(f):
    def wrapper(*args, **kwargs):
        return greenlet(f).switch(*args, **kwargs)
    return wrapper


def run(loop):
    try:
        import tornado.ioloop
        import tornado.gen
    except ImportError:
        pass
    else:
        if isinstance(loop, tornado.ioloop.IOLoop):
            local.make_coroutine = tornado.gen.coroutine
            local.schedule = lambda x: x
            local.main = greenlet(loop.start)
            return local.main.switch()

    try:
        import asyncio
    except ImportError:
        pass
    else:
        if isinstance(loop, asyncio.AbstractEventLoop):
            local.make_coroutine = asyncio.coroutine
            local.schedule = loop.create_task
            local.main = greenlet(loop.run_forever)
            return local.main.switch()

    raise ValueError('Invalid event loop provided')
