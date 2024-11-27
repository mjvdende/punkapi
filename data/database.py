import json
from collections import OrderedDict


FILE_PATH = "data/data.json"


def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file, object_pairs_hook=OrderedDict)

    return data


def get_db():
    return load_data(FILE_PATH)


def get_short_db():
    full_db = load_data(FILE_PATH)
    short_db = list()
    for beer in full_db:
        short_beer = dict()
        short_beer["id"] = beer.get("id")
        short_beer["name"] = beer.get("name")
        short_beer["tagline"] = beer.get("tagline")
        short_beer["first_brewed"] = beer.get("first_brewed")
        short_beer["description"] = beer.get("description")
        short_beer["image_url"] = beer.get("image_url")
        short_beer["abv"] = beer.get("abv")
        short_beer["ibu"] = beer.get("ibu")
        short_beer["ebc"] = beer.get("ebc")
        short_beer["food_pairing"] = beer.get("food_pairing")
        short_db.append(short_beer)

    return short_db



