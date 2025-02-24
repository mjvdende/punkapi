from typing import List, Optional, Dict
from punkapi.repository.repository import beer, random_beer, beers
from punkapi.db.models import Beer

class BeerService:
    async def get_beers(self, page: int, per_page: int, filters: Optional[Dict] = None) -> List[Beer]:
        return [Beer(**b) for b in beers({"page": page, "per_page": per_page, **filters} if filters else {})]

    async def get_beer_by_id(self, beer_id: int) -> Beer:
        result = beer(beer_id)
        if not result:
            raise ValueError(f"Beer with id {beer_id} not found")
        return Beer(**result)

    async def get_random_beer(self) -> Beer:
        return Beer(**random_beer())