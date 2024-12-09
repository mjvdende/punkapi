from fastapi import HTTPException
from fastapi.params import Path

from repository.repository import beer as punk_beer, beers_size

size = beers_size()


async def beer(beer_id: int = Path(..., ge=1, le=size)):
    print(f"API – /beers/{beer_id}")

    selected_beer = punk_beer(beer_id)
    if not selected_beer:
        raise HTTPException(
            status_code=404,
            detail={
                "error": "Not Found",
                "message": f"No beer found that matches the ID {beer_id}"
            }
        )

    return selected_beer
