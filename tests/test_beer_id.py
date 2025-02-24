import pytest

@pytest.mark.asyncio(loop_scope="session")
async def test_beer_by_id(client):
    beer_id = 1
    response = await client.get(f"/beers/{beer_id}")
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data, dict)
    assert json_data["id"] == beer_id

# negatief
@pytest.mark.asyncio(loop_scope="session")
async def test_invalid_beer_id(client):
    response = await client.get("/beers/416")
    assert response.status_code == 422 
    json_data = response.json()

    assert "detail" in json_data
    assert isinstance(json_data["detail"], list)
    assert json_data["detail"][0]["msg"] == "Input should be less than or equal to 415"