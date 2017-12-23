import facebook


def add_birthday_to_contacts(user, contact_list):
    user_graph = facebook.get_user_from_cookie()
    facebook.GraphAPI.get_connections(user, "friend_list")
    pass


def add_birthday_to_contact(user_facebook_token, contact_list, contact):
    pass


def get_user_birthday(user_facebook_token):
    pass


def get_user_friend_list(user_facebook_token):
    pass
