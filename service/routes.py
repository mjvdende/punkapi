from fastapi import APIRouter

from service.api.about import about
from service.api.image import image
from service.api.random import random_beer
from service.api.beer import beer
from service.api.beers import beers

api_router = APIRouter()

api_router.get("/img/{filename:path}")(image)
api_router.get("/random")(random_beer)
api_router.get("/beer")(beer)
api_router.get("/beers")(beers)
api_router.get("/")(about)
