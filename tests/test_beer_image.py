import pytest

@pytest.mark.asyncio(loop_scope="session")
async def test_beer_image(client):
    beer_id = 1
    response = await client.get(f"/images/{beer_id:03d}.png")
    assert response.status_code == 200
    assert response.headers["Content-Type"] in ["image/png", "image/jpeg"]