import aiohttp_jinja2
from aiohttp import web


# @aiohttp_jinja2.template("index.html")
# async def index(request):
#     return {'title': 'Пишем первое приложение на aiohttp'}


class Index(web.View):

    @aiohttp_jinja2.template("index.html")
    async def get(self):
        return {'title': 'test'} # web.Response(text='ЭЩКЕРЕЕ')

    # async def post(self):
    #     return await {'title': 'Пишем первое приложение на aiohttp'}

class testfile(web.View):
    async def post(self):
        return web.Response(text='test')