from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api
from werkzeug.exceptions import HTTPException

from service.routes import api_routes


cors_options = {
    "origins": "*",
    "supports_credentials": True,
    "expose_headers": [
        'x-ratelimit-limit',
        'x-ratelimit-remaining',
        'content-length',
        'origin',
        'content-type',
        'accept'
    ]
}

app = Flask(__name__)
app.json.sort_keys = False
api = Api(app)
CORS(app, **cors_options)


app.register_blueprint(api_routes, url_prefix='/v3')


@app.errorhandler(Exception)
def handle_exception(e):
    # Если это стандартная ошибка HTTP, возвращаем её
    if isinstance(e, HTTPException):
        return jsonify({
            "error": e.name,
            "message": e.description
        }), e.code

    # В противном случае возвращаем 500 с сообщением об ошибке
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
