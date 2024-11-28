from typing import Annotated

from fastapi import HTTPException
from fastapi.params import Query
from pydantic import BaseModel, Field

from repository.repository import beer as punk_beer, beers_size

size = beers_size()

class BeerSchema(BaseModel):
    id: int = Field(ge=1, le=size)  # Валидация, что id должен быть больше или равен 1 и меньше или равен 325


async def beer(params: Annotated[BeerSchema, Query()]):
    beer_id = params.id
    print(f"API – /beer?id={beer_id}")

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
