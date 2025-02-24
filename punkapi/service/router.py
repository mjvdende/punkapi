from fastapi import APIRouter

from punkapi.service.api.about import about
from punkapi.service.api.image import image
from punkapi.service.api.random import random_beer
from punkapi.service.api.beer import beer
from punkapi.service.api.beers import beers

api_router = APIRouter()

api_router.get("/images/{filename:path}")(image)
api_router.get("/beers/random")(random_beer)
api_router.get("/beers/{beer_id}")(beer)
api_router.get("/beers")(beers)
api_router.get("/")(about)
