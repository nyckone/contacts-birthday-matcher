import Levenshtein


def are_names_equal_with_max_distance(name1, name2, distance):
    return Levenshtein.distance(name1, name2) <= distance


def _is_either_name_contained(name1, name2):
    if name1 is None or name2 is None:
        return False

    if name1 in name2 or name2 in name1:
        return True


def is_contained_name(exact_name, name):
    found_splits = 0
    splitted_name = name.split()
    for part_name in splitted_name:
        if _is_either_name_contained(part_name, exact_name):
            found_splits += 1

    if found_splits >= 2:
        return True

    return False
