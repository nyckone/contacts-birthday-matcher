from name_utils import name_utils


def find_contained_name_contact(contact_list, friend_name):
    for contact in contact_list:
        contact_name = get_contact_name(contact)
        if name_utils.is_contained_name(friend_name, contact_name):
            return contact

    return None


def find_contact(contact_list, friend_name):
    for contact in contact_list:
        contact_name = get_contact_name(contact)
        if friend_name == contact_name:
            return contact

    return None


def find_contact_with_distance(contact_list, friend_name, distance):
    for contact in contact_list:
        contact_name = get_contact_name(contact)
        if name_utils.are_names_equal_with_max_distance(friend_name, contact_name, distance):
            return contact

    return None


def get_contact_name(contact):
    return contact


def get_contact_phone(contact_list, contact):
    return list(contact_list.keys())[list(contact_list.values()).index(contact)]


def add_birthday_to_contact(contact, contact_birthday):
    pass
