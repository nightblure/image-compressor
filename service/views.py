import aiohttp_jinja2
from aiohttp import web

from file_process import save_file, compress_file


class CompressImageView(web.View):
    async def post(self):
        return await compress_file(self.request)

    @aiohttp_jinja2.template('compress_page.html')
    async def get(self):
        pass