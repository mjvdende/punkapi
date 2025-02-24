from functools import reduce
from typing import List, Dict, Optional

from punkapi.repository.dao.filters import abv_gt_filter, abv_lt_filter
from punkapi.repository.dao.filters import beer_name_filter
from punkapi.repository.dao.filters import brewed_before_filter, brewed_after_filter
from punkapi.repository.dao.filters import ebc_gt_filter, ebc_lt_filter
from punkapi.repository.dao.filters import food_filter
from punkapi.repository.dao.filters import ibu_gt_filter, ibu_lt_filter
from punkapi.repository.dao.filters import ids_filter


def get_beer_by_id(val: Optional[int], db: List[Dict]) -> Optional[Dict]:
    if val is None:
        return None

    for beer in db:
        beer_id = beer.get('id')
        if beer_id == val:
            return beer

    return None


def get_beers_with_options(db: List[Dict], opts: Dict) -> List[Dict]:
    page = opts.get('page', 1)
    per_page = opts.get('per_page')

    ids = opts.get('ids')
    beer_name = opts.get('beer_name')
    brewed_before = opts.get('brewed_before')
    brewed_after = opts.get('brewed_after')
    abv_gt = opts.get('abv_gt')
    abv_lt = opts.get('abv_lt')
    ibu_gt = opts.get('ibu_gt')
    ibu_lt = opts.get('ibu_lt')
    ebc_gt = opts.get('ebc_gt')
    ebc_lt = opts.get('ebc_lt')
    food = opts.get('food')


    filter_functions = [
        ids_filter(ids),
        beer_name_filter(beer_name),
        brewed_before_filter(brewed_before),
        brewed_after_filter(brewed_after),
        abv_gt_filter(abv_gt),
        abv_lt_filter(abv_lt),
        ebc_gt_filter(ebc_gt),
        ebc_lt_filter(ebc_lt),
        ibu_gt_filter(ibu_gt),
        ibu_lt_filter(ibu_lt),
        food_filter(food),
    ]

    # Apply all filters
    filtered_beers = reduce(lambda acc, f: f(acc), filter_functions, db)

    # Apply pagination if parameters are present
    if per_page:
        start_idx = (page - 1) * per_page
        end_idx = start_idx + per_page
        return filtered_beers[start_idx:end_idx]

    return filtered_beers
