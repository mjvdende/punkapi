import pytest
from punkapi.repository import BeerRepository

def test_get_beers():
    repository = BeerRepository()
    beers = repository.get_beers(1, 10)
    assert len(beers) == 10
    assert all(isinstance(beer["id"], int) for beer in beers)