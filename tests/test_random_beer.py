import pytest

@pytest.mark.asyncio(loop_scope="session")
async def test_random_beer(client):
    response = await client.get("/beers/random")
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data, dict)
    assert "id" in json_data
    assert "name" in json_data
