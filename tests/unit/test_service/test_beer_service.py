import pytest
from punkapi.service import BeerService

@pytest.mark.asyncio
async def test_get_beers():
    service = BeerService()
    beers = await service.get_beers(1, 10)
    assert len(beers) == 10
    assert all(isinstance(beer.id, int) for beer in beers)