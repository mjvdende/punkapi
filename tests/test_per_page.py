import pytest

@pytest.mark.asyncio(loop_scope="session")
async def test_per_page_10(client):
    response = await client.get("/beers", params={"per_page": 10, "page": 1})
    assert response.status_code == 200
    assert len(response.json()) == 10

# grenswaarde
@pytest.mark.asyncio(loop_scope="session")
async def test_per_page_80(client):
    response = await client.get("/beers", params={"per_page": 80, "page": 1})
    assert response.status_code == 200
    assert len(response.json()) <= 80

@pytest.mark.asyncio(loop_scope="session")
async def test_per_page_below_min(client):
    response = await client.get("/beers", params={"per_page": 5})
    assert response.status_code == 422  

@pytest.mark.asyncio(loop_scope="session")
async def test_per_page_above_max(client):
    response = await client.get("/beers", params={"per_page": 100, "page": 1})
    assert response.status_code == 422 