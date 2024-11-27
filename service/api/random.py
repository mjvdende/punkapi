from flask import jsonify
from repository.repository import random_beer as punk_random

def random_beer():
    selected_beer = punk_random()
    print("API – /beers/random")
    return jsonify(selected_beer), 200
