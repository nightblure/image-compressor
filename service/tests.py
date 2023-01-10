"""Tests module."""
import json
from unittest import mock

import pytest
from aiohttp import web

from main import main
from views import testfile


@pytest.fixture()
def app(loop, aiohttp_client):
    app = main()
    return loop.run_until_complete(aiohttp_client(app))


@pytest.mark.asyncio
async def test_testfile(app):
    resp = await app.post('/test/')
    assert resp.status == 200
    text = await resp.text()
    assert {"detail": "test"} == json.loads(text)


# @pytest.mark.asyncio
# async def test_Index(app):
#     resp = await app.get('/')
#     assert resp.status == 200
#     text = await resp.text()
#     print(text)
#     assert 'test' in text
