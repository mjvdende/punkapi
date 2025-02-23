import pytest
from httpx import AsyncClient
from punkapi.app import app

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(base_url="http://localhost:5000") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"project": "https://github.com/alxiw/punkapi"}

@pytest.mark.asyncio
async def test_v3_endpoint():
    async with AsyncClient(base_url="http://localhost:5000") as ac:
        response = await ac.get("/v3/beers/random")
    assert response.status_code == 200



