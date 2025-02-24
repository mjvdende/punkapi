from jsonschema import validate
import pytest

beer_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "abv": {"type": "number"},
    },
    "required": ["id", "name"]
}

# contract
@pytest.mark.asyncio(loop_scope="session")
async def test_beer_schema(client):
    response = await client.get("/beers/random")
    assert response.status_code == 200
    json_data = response.json()  # De API geeft een lijst met 1 bier
    validate(instance=json_data, schema=beer_schema)

beer_schema_extended = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "abv": {"type": "number"},
        "description": {"type": "string"},
        "image_url": {"type": "string"},
        "ingredients": {
            "type": "object",
            "properties": {
                "malt": {"type": "array"},
                "hops": {"type": "array"},
                "yeast": {"type": "string"}
            }
        }
    },
    "required": ["id", "name", "description"]
}

@pytest.mark.asyncio(loop_scope="session")
async def test_beer_schema(client):
    response = await client.get("/beers/random")
    assert response.status_code == 200
    json_data = response.json()  # De API geeft een lijst met 1 bier
    validate(instance=json_data, schema=beer_schema_extended)