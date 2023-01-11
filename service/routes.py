from aiohttp import web

import settings
from views import CompressImageView


def setup_routes(app):
    routes = [
        web.get('/', CompressImageView),
        web.post('/compress/', CompressImageView, name='compress_route'),
    ]
    app.add_routes(routes)
