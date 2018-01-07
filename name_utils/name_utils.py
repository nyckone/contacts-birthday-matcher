import Levenshtein

MAJORITY_OF_NAME_SPLITS_EQUAL = 2


def are_names_equal_with_max_distance(name1, name2, distance):
    return Levenshtein.distance(name1, name2) <= distance


def _is_either_name_contained(name1, name2):
    if name1 in name2 or name2 in name1:
        return True


# Found splits need to be greater then 1 in order to return true since we have at least first name and last name that
# needs to be equal
def is_contained_name(exact_name, name):
    if exact_name is None or name is None:
        return False
    found_splits = 0
    splitted_name = name.split()
    for part_name in splitted_name:
        if _is_either_name_contained(part_name, exact_name):
            found_splits += 1

    if found_splits >= MAJORITY_OF_NAME_SPLITS_EQUAL:
        return True

    return False
