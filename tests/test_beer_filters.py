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