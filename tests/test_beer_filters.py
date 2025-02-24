import pytest

@pytest.mark.asyncio(loop_scope="session")
@pytest.mark.parametrize("param, value", [
    ("per_page", "50"),
    ("beer_name", "Punk"),
    ("ids", "1,2,3"),
    ("brewed_before", "12-2020"),
    ("brewed_after", "01-2010"),
    ("abv_gt", "5"),
    ("abv_lt", "10"),
    ("ibu_gt", "20"),
    ("ibu_lt", "50"),
    ("ebc_gt", "10"),
    ("ebc_lt", "40"),
    ("food", "burger")
])
async def test_beers_filters(client, param, value):
    response = await client.get(f"/beers?page=1&{param}={value}")
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data, list)

# idempotentie
@pytest.mark.asyncio(loop_scope="session")
async def test_consistent_beer_name_filter(client):
    response1 = await client.get("/beers?page=1&beer_name=Punk")
    response2 = await client.get("/beers?page=1&beer_name=Punk")
    assert response1.json() == response2.json()

# error handling
@pytest.mark.asyncio(loop_scope="session")
async def test_invalid_date_format(client):
    response = await client.get("/beers", params={"brewed_before": "invalid-date"})
    assert response.status_code == 422

@pytest.mark.asyncio(loop_scope="session")
async def test_invalid_number_format(client):
    response = await client.get("/beers", params={"abv_gt": "not-a-number"})
    assert response.status_code == 422

# combintion of filters
@pytest.mark.asyncio(loop_scope="session")
async def test_multiple_filters(client):
    response = await client.get("/beers", params={
        "page": "1",
        "abv_gt": "5",
        "ibu_gt": "30",
        "per_page": "20"
    })
    assert response.status_code == 200
    data = response.json()
    assert all(beer["abv"] > 5 for beer in data)
    assert all(beer["ibu"] > 30 for beer in data)