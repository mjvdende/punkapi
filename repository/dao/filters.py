from repository.utils.curry import curry
from repository.utils.date import is_date_after
from repository.utils.date import is_date_before
from repository.utils.string import string_fuzzy_match, string_match

from typing import List, Dict, Optional


def beer_name_filter(val: Optional[str], db: List[Dict]) -> List[Dict]:
    if val is None:
        return db

    return [
        beers for beers in db
        if string_fuzzy_match(beers['name'], val)
    ]


def brewed_before_filter(val: Optional[str], db: List[Dict]) -> List[Dict]:
    if val is None:
        return db

    return [
        beers for beers in db
        if is_date_before(beers['first_brewed'], val)
    ]


def brewed_after_filter(val: Optional[str], db: List[Dict]) -> List[Dict]:
    if val is None:
        return db

    return [
        beers for beers in db
        if is_date_after(beers['first_brewed'], val)
    ]


def abv_gt_filter(val, database):
    if val is None:
        return database

    return [
        beers for beers in database
        if beers.get('abv', 0)  > val
    ]


def abv_lt_filter(val, database):
    if val is None:
        return database

    return [
        beers for beers in database
        if beers.get('abv', 0) < val
    ]


def ibu_gt_filter(val, database):
    if val is None:
        return database

    return [
        beers for beers in database
        if beers.get("ibu") is not None and beers["ibu"] > val
    ]


def ibu_lt_filter(val, database):
    if val is None:
        return database

    return [
        beers for beers in database
        if beers.get("ibu") is not None and beers["ibu"] < val
    ]


def ebc_gt_filter(val, database):
    if val is None:
        return database

    return [
        beers for beers in database
        if beers.get("ebc") is not None and beers["ebc"] > val
    ]


def ebc_lt_filter(val, database):
    if val is None:
        return database

    return [
        beers for beers in database
        if beers.get("ebc") is not None and beers["ebc"] < val
    ]


def food_filter(val: Optional[str], db: List[Dict]) -> List[Dict]:
    """Фильтрует список, возвращая элементы, у которых food_pairing соответствует val."""
    if val is None:
        return db

    return [
        beer for beer in db
        if any(string_match(o, val) for o in beer.get('food_pairing', []))
    ]


def ids_filter(val: Optional[str], db: List[Dict]) -> List[Dict]:
    """Фильтрует список, возвращая элементы, id которых содержится в val."""
    if val is None:
        return db

    id_array = list(map(int, val.split(",")))
    return [
        beers for beers in db
        if beers['id'] in id_array
    ]


beer_name_filter = curry(beer_name_filter)
brewed_before_filter = curry(brewed_before_filter)
brewed_after_filter = curry(brewed_after_filter)
abv_gt_filter = curry(abv_gt_filter)
abv_lt_filter = curry(abv_lt_filter)
ibu_gt_filter = curry(ibu_gt_filter)
ibu_lt_filter = curry(ibu_lt_filter)
ebc_gt_filter = curry(ebc_gt_filter)
ebc_lt_filter = curry(ebc_lt_filter)
food_filter = curry(food_filter)
ids_filter = curry(ids_filter)
