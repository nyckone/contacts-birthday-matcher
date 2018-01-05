from contact_utils import contact_utils

MAX_DISTANCE = 3


def _find_distanced_contact_birthday(name_birthday_list, friend_name):
    return contact_utils.find_distanced_contact_birthday(name_birthday_list, friend_name, MAX_DISTANCE)


def _add_birthday_of_found_name(name_birthday_dict, contact_dict, find_name_function, contact_with_birthday_dict):
    for phone_number, contact_name in contact_dict.iteritems():
        if phone_number not in contact_with_birthday_dict:
            contact_birthday = find_name_function(name_birthday_dict, contact_name)
            if contact_birthday:
                contact_with_birthday_dict[phone_number] = (contact_name, contact_birthday)


def add_birthday_to_contacts(name_birthday_list, contact_list):
    contact_with_birthday_dict = dict()
    _add_birthday_of_found_name(name_birthday_list, contact_list, contact_utils.find_exact_contact_birthday,
                                contact_with_birthday_dict)
    _add_birthday_of_found_name(name_birthday_list, contact_list, contact_utils.find_contained_contact_birthday,
                                contact_with_birthday_dict)
    _add_birthday_of_found_name(name_birthday_list, contact_list, _find_distanced_contact_birthday,
                                contact_with_birthday_dict)

    return contact_with_birthday_dict
