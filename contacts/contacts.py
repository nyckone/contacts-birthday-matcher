from contact_utils import contact_utils

MAX_DISTANCE = 3


def _find_distanced_contact(name_birthday_list, friend_name):
    return contact_utils.find_distanced_contact(name_birthday_list, friend_name, MAX_DISTANCE)


# This function adds a phone_number -> (name_in_contacts, exact_name, birthday)
# we assume that the name_birthday_dict names are accurate. and we return the name as it appears in contacts as well
# so we will be able to keep that name in contacts.
def _add_birthday_of_found_name(name_birthday_dict, contact_dict, find_name_function, contact_with_birthday_dict):
    for exact_name, user_birthday in name_birthday_dict.iteritems():
        contact_phone_number, name_in_contacts = find_name_function(contact_dict, exact_name)
        if contact_phone_number and (contact_phone_number not in contact_with_birthday_dict):
            contact_with_birthday_dict[contact_phone_number] = (name_in_contacts, exact_name, user_birthday)


def add_birthday_to_contacts(name_birthday_list, contact_list):
    contact_with_birthday_dict = dict()
    _add_birthday_of_found_name(name_birthday_list, contact_list, contact_utils.find_exact_contact,
                                contact_with_birthday_dict)
    _add_birthday_of_found_name(name_birthday_list, contact_list, contact_utils.find_contained_contact,
                                contact_with_birthday_dict)
    _add_birthday_of_found_name(name_birthday_list, contact_list, _find_distanced_contact,
                                contact_with_birthday_dict)

    return contact_with_birthday_dict
