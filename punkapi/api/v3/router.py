from fastapi import APIRouter
from punkapi.api.v3.endpoints import beers, images

api_router = APIRouter(prefix="/v3")

# Include sub-routers
api_router.include_router(beers.router, tags=["beers"])
api_router.include_router(images.router, tags=["images"])