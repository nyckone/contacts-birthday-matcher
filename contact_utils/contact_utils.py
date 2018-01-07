from name_utils import name_utils


def find_contained_contact(contact_dict, exact_name):
    for phone_number, name in contact_dict.iteritems():
        if name_utils.is_contained_name(exact_name, name):
            return phone_number, name

    return None


def find_exact_contact(contact_dict, exact_name):
    for phone_number, name in contact_dict.iteritems():
        if exact_name == name:
            return phone_number, name

    return None


def find_distanced_contact(contact_dict, exact_name, distance):
    for phone_number, name in contact_dict.iteritems():
        if name_utils.are_names_equal_with_max_distance(exact_name, name, distance):
            return phone_number, name

    return None
