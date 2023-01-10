import os

from aiohttp import web
from multidict import MultiDict

import settings


async def save_file(request):
    reader = await request.multipart()
    field = await reader.next()
    filename = field.filename
    size = 0
    path = os.path.join(settings.SERVICE_FILES_DIR, filename)

    with open(path, 'wb') as file:
        while True:
            chunk = await field.read_chunk()  # 8192 bytes by default.
            if not chunk:
                break
            size += len(chunk)
            file.write(chunk)

    # region OLD CODE (unsafe because aiohttp docs)
    # https://docs.aiohttp.org/en/stable/web_quickstart.html?highlight=file%20#file-uploads
    # data = await request.post()
    # file = data['file']
    # filename = file.filename
    # content = file.file.read()
    #
    # with open(path, 'wb') as file_desc:
    #     file_desc.write(content)
    # endregion

    return web.FileResponse(path=path)