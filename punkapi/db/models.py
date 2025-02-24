from typing import List, Optional
from pydantic import BaseModel, Field

class Temperature(BaseModel):
    value: Optional[float]
    unit: str

class Volume(BaseModel):
    value: int
    unit: str

class MashTemp(BaseModel):
    temp: Temperature
    duration: Optional[float] = None

class Fermentation(BaseModel):
    temp: Temperature

class Method(BaseModel):
    mash_temp: List[MashTemp]
    fermentation: Fermentation
    twist: Optional[str] = None

class Amount(BaseModel):
    value: float
    unit: str

class Malt(BaseModel):
    name: str
    amount: Amount

class Hop(BaseModel):
    name: str
    amount: Amount
    add: str
    attribute: Optional[str] = None

class Ingredients(BaseModel):
    malt: List[Malt]
    hops: List[Hop]
    yeast: Optional[str] = None

class Beer(BaseModel):
    id: int
    name: str
    tagline: str
    first_brewed: str
    description: str
    image: str
    abv: float
    ibu: Optional[float] = None
    target_fg: Optional[float] = None
    target_og: Optional[float] = None
    ebc: Optional[float] = None
    srm: Optional[float] = None
    ph: Optional[float] = None
    attenuation_level: Optional[float] = None
    volume: Volume
    boil_volume: Volume
    method: Method
    ingredients: Ingredients
    food_pairing: List[str]
    brewers_tips: str
    contributed_by: str