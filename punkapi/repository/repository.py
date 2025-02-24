import random
from typing import Optional, Dict, List

from punkapi.db.database import get_db
from punkapi.repository.dao.dao import get_beer_by_id, get_beers_with_options

full_db = get_db()
sorted_db = sorted(get_db(), key=lambda x: x['id'])


def random_beer() -> Optional[Dict]:
    return random.choice(sorted_db)


def beer(beer_id) -> Optional[Dict]:
    return get_beer_by_id(beer_id, full_db)


def beers(options=None) -> List[Dict]:
    if options is None:
        options = {}
    return get_beers_with_options(sorted_db, options)


def beers_size() -> int:
    return len(sorted_db)
