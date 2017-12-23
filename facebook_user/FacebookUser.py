import facebook


class FacebookUser(object):
    def __init__(self, facebook_token):
        self._facebook_access_token = facebook_token

    def get_friend_list(self):
        pass

    def get_birthday(self):
        pass

    def get_name(self):
        pass
