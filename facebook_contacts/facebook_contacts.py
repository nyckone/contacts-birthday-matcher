import facebook

from contact_utils import contact_utils
from facebook_user import FacebookUser

MAX_DISTANCE = 3


def add_birthday_to_contacts(user_facebook_token, contact_list):
    facebook_user = FacebookUser.FacebookUser(user_facebook_token)
    friend_list = facebook_user.get_friend_list()

    for friend in friend_list:
        friend_facebook_token = get_facebook_token(friend)
        friend_facebook_user = FacebookUser.FacebookUser(friend_facebook_token)
        add_birthday_if_contact_exist(friend_facebook_user, contact_list)


def find_contact_phone(contact_list, friend_name):
    contact = contact_utils.find_contact(contact_list, friend_name)
    if not contact:
        contact = contact_utils.find_contained_name_contact(contact_list, friend_name)

    if not contact:
        contact = contact_utils.find_contact_with_distance(contact_list, friend_name, MAX_DISTANCE)

    if contact:
        return contact_utils.get_contact_phone(contact_list, contact)

    return None


def add_birthday_if_contact_exist(friend_facebook_user, contact_list):
    friend_name = friend_facebook_user.get_name()
    is_contact_found, contact_phone = find_contact_phone(contact_list, friend_name)
    if is_contact_found:
        friend_birthday = friend_facebook_user.get_birthday()
        updated_contact = contact_utils.add_birthday_to_contact(contact_list[contact_phone], friend_birthday)
        contact_list[contact_phone] = updated_contact


def get_facebook_token(friend):
    pass
