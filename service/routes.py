from flask import Blueprint

from service.api.about import about
from service.api.image import image
from service.api.random import random_beer
from service.api.beer import beer
from service.api.beers import beers

api_routes = Blueprint('api', __name__)

api_routes.route('/img/<path:filename>', methods=['GET'])(image)
api_routes.route('/random', methods=['GET'])(random_beer)
api_routes.route('/beer', methods=['GET'])(beer)
api_routes.route('/beers', methods=['GET'])(beers)
api_routes.route('/', methods=['GET'])(about)
