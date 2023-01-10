from aiohttp import web

from views import Index, testfile


def setup_routes(app):
    routes = [
        web.get('/', Index),
        web.post('/test/', testfile)
    ]
    app.add_routes(routes)
