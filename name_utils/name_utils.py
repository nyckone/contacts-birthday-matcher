import Levenshtein

MAJORITY_OF_NAME_SPLITS_EQUAL = 2


def are_names_equal_with_max_distance(name1, name2, distance):
    return Levenshtein.distance(name1, name2) <= distance


# Found splits need to be greater then 1 in order to return true since we have at least first name and last name that
# needs to be equal
def _is_first_contained(contained_name, full_name):
    if full_name is None or contained_name is None:
        return False
    found_splits = 0
    splitted_name = contained_name.split()
    for part_name in splitted_name:
        if part_name in full_name:
            found_splits += 1

    if found_splits >= MAJORITY_OF_NAME_SPLITS_EQUAL:
        return True

    return False


def is_contained_name(exact_name, name):
    return _is_first_contained(exact_name, name) or _is_first_contained(name, exact_name)