import aiohttp_cors
import aiohttp_jinja2
import jinja2
from aiohttp import web

from service.routes import setup_routes


def build_app():
    application = web.Application()
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


def main(argv):
    app = build_app()
    web.run_app(app)


# https://docs.aiohttp.org/en/stable/web_quickstart.html#run-a-simple-web-server
# CMD RUN COMMAND: python -m aiohttp.web -H localhost -P 8080 service.main:main
# MAIN URL: http://localhost:8080/
if __name__ == '__main__':
    argv = []
    main(argv)
