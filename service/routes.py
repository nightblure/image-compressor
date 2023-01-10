from aiohttp import web

from views import Index, testfile
from file_loader import save_file


def setup_routes(app):
    routes = [
        web.get('/', Index),
        web.post('/test/', save_file)
    ]
    app.add_routes(routes)
