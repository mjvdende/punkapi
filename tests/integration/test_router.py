import pytest
from fastapi.testclient import TestClient
from punkapi.app import app

@pytest.fixture
def client():
    return TestClient(app)

class TestBeerRouter:
    def test_get_beers_with_pagination(self, client):
        response = client.get("/v3/beers?page=1&per_page=10")
        assert response.status_code == 200
        assert len(response.json()) == 10

    def test_get_beer_by_id(self, client):
        response = client.get("/v3/beers/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1

    def test_get_beer_not_found(self, client):
        response = client.get("/v3/beers/9999")
        assert response.status_code == 422

    def test_get_random_beer(self, client):
        response = client.get("/v3/beers/random")
        assert response.status_code == 200
        assert "id" in response.json()

    def test_invalid_pagination(self, client):
        response = client.get("/v3/beers?per_page=5")
        assert response.status_code == 422

    def test_beer_name_filter(self, client):
        response = client.get("/v3/beers?page=1&beer_name=IPA")
        assert response.status_code == 200