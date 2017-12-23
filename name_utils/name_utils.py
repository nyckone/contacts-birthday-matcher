import Levenshtein

FIRST_NAME = 0
LAST_NAME = 1


def are_names_equal_with_max_distance(name1, name2, distance):
    return Levenshtein.distance(name1, name2) <= distance


def parse_full_name(full_name, position):
    full_name_array = full_name.split()
    if len(full_name_array) > position:
        return full_name_array[position]


def compare_two_full_names(full_name1, full_name2, first_name_distance=0, last_name_distance=0):
    first_name1 = parse_full_name(full_name1, FIRST_NAME)
    first_name2 = parse_full_name(full_name2, FIRST_NAME)

    last_name1 = parse_full_name(full_name1, LAST_NAME)
    last_name2 = parse_full_name(full_name2, LAST_NAME)

    return are_names_equal_with_max_distance(first_name1, first_name2, first_name_distance) and \
           are_names_equal_with_max_distance(last_name1, last_name2, last_name_distance)