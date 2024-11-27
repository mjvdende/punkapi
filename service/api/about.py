from flask import jsonify


def about():
    response = jsonify({"project": "punkapi", "author": "alxiw"})

    return response, 200

