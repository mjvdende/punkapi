from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from punkapi.service.beer_service import BeerService
from punkapi.db.models import Beer

router = APIRouter()
beer_service = BeerService()

@router.get("/beers", response_model=List[Beer])
async def get_beers(
    page: int = Query(1, ge=1),
    per_page: int = Query(30, ge=10, le=80),
    beer_name: Optional[str] = None,
):
    return await beer_service.get_beers(page, per_page, {"beer_name": beer_name})

@router.get("/beers/random", response_model=Beer)
async def get_random_beer():
    return await beer_service.get_random_beer()

@router.get("/beers/{beer_id}", response_model=Beer)
async def get_beer(beer_id: int):
    try:
        return await beer_service.get_beer_by_id(beer_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Beer not found")