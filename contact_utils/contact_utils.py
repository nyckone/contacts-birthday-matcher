from name_utils import name_utils


def find_contained_contact_birthday(name_birthday_dict, friend_name):
    for name, birthday in name_birthday_dict.iteritems():
        if name_utils.is_contained_name(friend_name, name):
            return birthday

    return None


def find_exact_contact_birthday(name_birthday_dict, friend_name):
    for name, birthday in name_birthday_dict.iteritems():
        if friend_name == name:
            return birthday

    return None


def find_distanced_contact_birthday(name_birthday_dict, friend_name, distance):
    for name, birthday in name_birthday_dict.iteritems():
        if name_utils.are_names_equal_with_max_distance(friend_name, name, distance):
            return birthday

    return None
