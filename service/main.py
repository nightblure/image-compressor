import aiohttp_cors
import aiohttp_jinja2
import jinja2
from aiohttp import web

from routes import setup_routes


def build_app():
    # megabytes
    MAX_MB_FILE_SIZE = 100
    application = web.Application(client_max_size=1024*1024*MAX_MB_FILE_SIZE)
    aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader("templates"))
    setup_routes(application)
    return application


# cors = aiohttp_cors.setup(app, defaults={
#     "*": aiohttp_cors.ResourceOptions(
#             allow_credentials=True,
#             expose_headers="*",
#             allow_headers="*",
#         )
# })
#
# for route in list(app.router.routes()):
#     cors.add(route)


def main(*args):
    app = build_app()
    return app


# https://docs.aiohttp.org/en/stable/web_quickstart.html#run-a-simple-web-server
# CMD RUN COMMAND: python -m aiohttp.web -H localhost -P 8080 service.main:main
# MAIN URL: http://localhost:8080/
# RUN WITH DEV-TOOLS (from service directory): adev runserver --app-factory main --port 8080
# RUN TESTS (from root directory): pytest -rs service/tests.py --cov=service
if __name__ == '__main__':
    app = build_app()
    web.run_app(app)

