from typing import List, Optional

from fastapi import Query
from pydantic import BaseModel, Field

from repository.repository import beers as punk_beers

DATE_PATTERN = r"^((0[1-9]|1[0-2])-)?\d{4}$"

class BeersSchema(BaseModel):
    page: int = Field(gt=0)
    per_page: int = Field(30, ge=10, le=80)
    abv_gt: Optional[float] = None
    abv_lt: Optional[float] = None
    ibu_gt: Optional[float] = None
    ibu_lt: Optional[float] = None
    ebc_gt: Optional[float] = None
    ebc_lt: Optional[float] = None
    brewed_before: Optional[str] = Field(None, pattern=DATE_PATTERN)
    brewed_after: Optional[str] = Field(None, pattern=DATE_PATTERN)
    beer_name: Optional[str] = None
    food: Optional[str] = None


async def beers(params: BeersSchema = Query(...)):
    options = dict(params)
    print(f"API – /beers, {options}")

    filtered_db = punk_beers(options)
    paginated_beers = paginate(filtered_db, params.page, params.per_page)

    return paginated_beers

def paginate(db: List, page: int, per_page: int) -> List:
    page_number = int(page) if page else 1
    per_page = int(per_page) if per_page else 30

    offset = (page_number - 1) * per_page

    return db[offset:offset + per_page]
