import json
import os
from collections import OrderedDict

DIRECTORY_PATH = "data"


def load_data_from_directory(directory_path):
    full_data = []

    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r') as file:
                data = json.load(file, object_pairs_hook=OrderedDict)
                full_data.append(data)

    return full_data


def get_db():
    return load_data_from_directory(DIRECTORY_PATH)


def get_short_db():
    full_db = load_data_from_directory(DIRECTORY_PATH)
    short_db = list()
    for beer in full_db:
        short_beer = dict()
        short_beer["id"] = beer.get("id")
        short_beer["name"] = beer.get("name")
        short_beer["tagline"] = beer.get("tagline")
        short_beer["first_brewed"] = beer.get("first_brewed")
        short_beer["description"] = beer.get("description")
        short_beer["image"] = beer.get("image")
        short_beer["abv"] = beer.get("abv")
        short_beer["ibu"] = beer.get("ibu")
        short_beer["ebc"] = beer.get("ebc")
        short_beer["food_pairing"] = beer.get("food_pairing")
        short_db.append(short_beer)

    return short_db



