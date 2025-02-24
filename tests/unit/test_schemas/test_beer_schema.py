import pytest
from punkapi.db.models import Beer

def test_beer_schema():
    beer_data = {
        "id": 1,
        "name": "Buzz",
        "tagline": "A Real Bitter Experience.",
        "first_brewed": "09/2007",
        "description": "A light, crisp and bitter IPA...",
        "image": "001.png",
        "abv": 4.5,
        "ibu": 60,
        "target_fg": 1010,
        "target_og": 1044,
        "ebc": 20,
        "srm": 10,
        "ph": 4.4,
        "attenuation_level": 75,
        "volume": {
            "value": 20,
            "unit": "litres"
        },
        "boil_volume": {
            "value": 25,
            "unit": "litres"
        },
        "method": {
            "mash_temp": [{
                "temp": {
                    "value": 64,
                    "unit": "celsius"
                },
                "duration": 75
            }],
            "fermentation": {
                "temp": {
                    "value": 19,
                    "unit": "celsius"
                }
            },
            "twist": None
        },
        "ingredients": {
            "malt": [{
                "name": "Maris Otter Extra Pale",
                "amount": {
                    "value": 3.3,
                    "unit": "kilograms"
                }
            }],
            "hops": [{
                "name": "Fuggles",
                "amount": {
                    "value": 25,
                    "unit": "grams"
                },
                "add": "start",
                "attribute": "bitter"
            }],
            "yeast": "Wyeast 1056 - American Ale™"
        },
        "food_pairing": [
            "Spicy chicken tikka masala",
            "Grilled chicken quesadilla",
            "Caramel toffee cake"
        ],
        "brewers_tips": "The earthy and floral aromas from the hops can be achieved through dry hopping.",
        "contributed_by": "Sam Mason <samjbmason>"
    }
    
    beer = Beer.model_validate(beer_data)
    assert beer.id == 1
    assert beer.name == "Buzz"
    assert beer.abv == 4.5
    assert len(beer.food_pairing) == 3