import re

def fuzzy_match(string: str, pattern: str) -> bool:
    pattern = ''.join(f'[^ {b}]*{b}' for b in pattern)
    regex = re.compile(pattern)

    return bool(regex.search(string))


def string_fuzzy_match(string: str, predicate: str) -> bool:
    if string is None or predicate is None:
        return False

    parsed_string = string.lower()
    parsed_predicate = predicate.lower().replace("_", " ")

    return fuzzy_match(parsed_string, parsed_predicate)


def string_match(string: str, predicate: str) -> bool:
    if string is None or predicate is None:
        return False

    parsed_string = string.lower()
    parsed_predicate = predicate.lower().replace("_", " ")

    return parsed_predicate in parsed_string

# Примеры использования
# print(string_fuzzy_match("Hello World", "Hlo Wrld"))   # True
# print(string_match("Hello World", "Hello"))            # True
# print(string_match("Hello World", "Hello_"))           # False
