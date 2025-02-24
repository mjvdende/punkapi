import pytest

@pytest.mark.asyncio(loop_scope="session")
async def test_root(client):
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"project": "https://github.com/alxiw/punkapi"}

@pytest.mark.asyncio(loop_scope="session")
async def test_v3_endpoint(client):
    response = await client.get("/v3/beers/random")
    assert response.status_code == 200

