from flask import jsonify, request
from marshmallow import ValidationError, Schema, fields

from repository.repository import beer as punk_beer, beers_size


def beer():
    size = beers_size()
    schema = BeerSchema()
    try:
        args = schema.load(request.args)
    except ValidationError as err:
        return jsonify({
            "error": f"Invalid query id param, must be an integer between 1 and {size}",
            "message": err.messages
        }), 400

    beer_id = args.get('id')

    # # Валидация beer_id
    #
    # if not isinstance(beer_id, int) or beer_id < 1 or beer_id > size:
    #     return jsonify({
    #         "error": "Invalid beer ID",
    #         "message": f"beer_id must be an integer between 1 and {size}"
    #     }), 400

    selected_beer = punk_beer(beer_id)

    if not selected_beer:
        return jsonify({
            "error": "Not Found",
            "message": f"No beer found that matches the ID {beer_id}"
        }), 404  # Возвращаем статус 404 Not Found

    #if not selected_beer:
        #return ValidationError(f"No beer found that matches the ID {beer_id}")

    print(f"API – /beers/{{id}} – {beer_id}")
    return jsonify(selected_beer), 200


class BeerSchema(Schema):
    id = fields.Int(
        required=True,
        validate=lambda n: 1 <= n <= 325,
        error_messages={"required": "Must be a number greater than 0 and less than 325"}
    )

