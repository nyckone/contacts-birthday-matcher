import facebook


class FacebookUser(object):
    def __init__(self, facebook_token):
        self._facebook_token = facebook_token

    def get_friend_list(self):
        pass

    def get_birthday(self):
        pass
