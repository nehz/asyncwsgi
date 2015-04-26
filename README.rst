asyncwsgi
==========
``asyncwsgi`` is a simple package for tornado and asyncio(WIP) to enable the
use of the WSGI interface asynchronously. Behind the scenes ``greenlet`` is
used to pause and resume each request.


Usage
------
#. Decorate functions that require async with ``asyncwsgi.coroutine``
#. Use ``asyncwsgi.wrap`` to wrap the WSGI container.
#. Run the event loop using ``asyncwsgi.run``



Examples
---------

Django ::

    @asyncwsgi.coroutine
    def my_view(request):
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch('http://www.google.com/')
        return render(request, 'my_view.html', {'code': response.code})

    ...
    # Patch django to run on tornado's event loop
    def run(host, port, app, **options):
        container = asyncwsgi.wrap(WSGIContainer(app))
        http_server = HTTPServer(container)
        http_server.listen(port, host)
        asyncwsgi.run(IOLoop.current())

    if __name__ == "__main__":
        ...
        from django.core.management.commands import runserver
        runserver.run = run

Bottle ::

    import asyncwsgi
    import bottle
    from tornado.httpclient import AsyncHTTPClient
    from tornado.wsgi import WSGIContainer
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop

    @bottle.get('/')
    @asyncwsgi.coroutine
    def index():
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch('http://www.google.com/')
        return 'Status: %d' % response.code

    container = asyncwsgi.wrap(WSGIContainer(bottle.default_app()))
    http_server = HTTPServer(container)
    http_server.listen(8080)
    asyncwsgi.run(IOLoop.current())


Installation
-------------
``pip install asyncwsgi``


Todo
-----
* asyncio not fully supported


License
--------
MIT licensed. See LICENSE for details.
