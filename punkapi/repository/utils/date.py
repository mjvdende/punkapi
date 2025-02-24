from datetime import datetime
from typing import Optional


def parse_date(date_str: str) -> Optional[datetime]:
    for f in ("%m/%Y", "%Y", "%m-%Y"):
        try:
            return datetime.strptime(date_str, f)
        except ValueError:
            continue
    return None


def is_date_before(brew_date: str, predicate: str) -> bool:
    parsed_brew_date = parse_date(brew_date)
    parsed_predicate = parse_date(predicate)

    if parsed_brew_date is None or parsed_predicate is None:
        return False

    return parsed_brew_date < parsed_predicate

def is_date_after(brew_date: str, predicate: str) -> bool:
    parsed_brew_date = parse_date(brew_date)
    parsed_predicate = parse_date(predicate)

    if parsed_brew_date is None or parsed_predicate is None:
        return False

    return parsed_brew_date > parsed_predicate
