import os

import PIL
import aiohttp_jinja2
from PIL import Image
from aiohttp import web

import settings

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


def allowed_file(extension):
    return extension in ALLOWED_EXTENSIONS


async def save_file(request):
    reader = await request.multipart()
    field = await reader.next()
    filename = field.filename
    size = 0
    path = os.path.join(settings.SERVICE_FILES_DIR, filename)

    extension = os.path.splitext(filename)[1]

    if not allowed_file(extension.split('.')[1]):
        return web.json_response({'detail': f'{extension} extension is not correct. please upload an image file'})

    if not os.path.exists(settings.SERVICE_FILES_DIR):
        os.mkdir(settings.SERVICE_FILES_DIR)

    with open(path, 'wb') as file:
        chunk = 10
        while chunk:
            chunk = await field.read_chunk()  # 8192 bytes by default.
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

    # return web.FileResponse(path=path)
    return path


@aiohttp_jinja2.template('compress_response.html')
async def compress_file(request):
    filename = await save_file(request)
    compress_img_path = compress_image(filename)
    print(filename, compress_img_path)
    return {'filename': os.path.basename(compress_img_path), 'imagepath': compress_img_path}
    # return web.HTTPFound(location=get_url_by_route_name(request.app.router, 'test_route'))


def compress_image(image_path):
    img = PIL.Image.open(image_path)
    height, width = img.size
    compress_img = img.resize((height, width), PIL.Image.ANTIALIAS)
    compress_img_name = f'compress_{os.path.basename(image_path)}'
    compress_img_path = f'{os.path.join(settings.SERVICE_FILES_DIR, compress_img_name)}'
    compress_img.save(compress_img_path)
    return compress_img_path
