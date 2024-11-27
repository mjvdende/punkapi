from datetime import datetime


def is_date_before(brew_date: str, predicate: str) -> bool:
    try:
        parsed_brew_date = datetime.strptime(brew_date, "%m/%Y")
        parsed_predicate = datetime.strptime(predicate, "%m-%Y")
    except ValueError:
        return False

    return parsed_brew_date < parsed_predicate


def is_date_after(brew_date: str, predicate: str) -> bool:
    try:
        parsed_brew_date = datetime.strptime(brew_date, "%m/%Y")
        parsed_predicate = datetime.strptime(predicate, "%m-%Y")
    except ValueError:
        return False

    return parsed_brew_date > parsed_predicate


# Примеры использования
# print(is_date_before("01/2020", "02-2020"))  # True
# print(is_date_after("01/2020", "02-2020"))   # False
