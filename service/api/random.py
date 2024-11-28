from fastapi.responses import JSONResponse
from repository.repository import random_beer as punk_random


async def random_beer():
    selected_beer = punk_random()
    print("API – /random")

    return JSONResponse(content=selected_beer)
