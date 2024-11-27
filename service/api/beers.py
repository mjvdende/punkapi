import re
from flask import request, jsonify, Request
from marshmallow import Schema, ValidationError, fields
from typing import List

from repository.repository import beers as punk_beers


def beers():
    schema = BeersSchema()
    try:
        args = schema.load(request.args)
    except ValidationError as err:
        return jsonify({
            "error": "Invalid query params",
            "message": err.messages
        }), 400

    filtered_db = punk_beers(args)
    paginated_beers = paginate(filtered_db, request)

    print(f"API – /beers – {dict(args)}")
    return jsonify(paginated_beers), 200


def paginate(db: List, req: Request) -> List:
    page = req.args.get('page')
    per_page = req.args.get('per_page')

    # Устанавливаем значения по умолчанию
    per_page = int(per_page) if per_page else 30
    page_number = int(page) if page else 1

    # Вычисляем смещение
    offset = (page_number - 1) * per_page

    # Возвращаем срез данных
    return db[offset:offset + per_page]


class BeersSchema(Schema):
    page = fields.Int(
        required=True,
        validate=lambda n: n > 0,
        error_messages={"required": "Must be a number greater than 0"}
    )
    per_page = fields.Int(
        required=False,
        validate=lambda n: 10 <= n <= 80,
        error_messages={"required": "Must be a number greater than 10 and less than 80"}
    )
    abv_gt = fields.Float(
        required=False,
        validate=lambda n: n > 0,
        error_messages={"required": "Must be a number greater than 0"}
    )
    abv_lt = fields.Float(
        required=False,
        validate=lambda n: n > 0,
        error_messages={"required": "Must be a number greater than 0"}
    )
    ibu_gt = fields.Float(
        required=False,
        validate=lambda n: n > 0,
        error_messages={"required": "Must be a number greater than 0"}
    )
    ibu_lt = fields.Float(
        required=False,
        validate=lambda n: n > 0,
        error_messages={"required": "Must be a number greater than 0"}
    )
    ebc_gt = fields.Float(
        required=False,
        validate=lambda n: n > 0,
        error_messages={"required": "Must be a number greater than 0"}
    )
    ebc_lt = fields.Float(
        required=False,
        validate=lambda n: n > 0,
        error_messages={"required": "Must be a number greater than 0"}
    )
    brewed_before = fields.Str(
        required=False,
        validate=lambda s: bool(re.match(r'^[0-1][0-9]-\d{4}$', s)),
        error_messages={"required": "Must be in date format of mm/yyyy"}
    )
    brewed_after = fields.Str(
        required=False,
        validate=lambda s: bool(re.match(r'^[0-1][0-9]-\d{4}$', s)),
        error_messages={"required": "Must be in date format of mm/yyyy"}
    )
    beer_name = fields.Str(
        required=False,
        validate=lambda s: bool(s.strip()),
        error_messages={"required": "Must have a value and if you are using multiple words use underscores to separate"}
    )
    food = fields.Str(
        required=False,
        validate=lambda s: bool(s.strip()),
        error_messages={"required": "Must have a value and if you are using multiple words use underscores to separate"}
    )
