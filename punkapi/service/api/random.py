from fastapi.responses import JSONResponse
from punkapi.repository.repository import random_beer as punk_random


async def random_beer():
    print("API – /beers/random")

    selected_beer = punk_random()

    return JSONResponse(content=selected_beer)
