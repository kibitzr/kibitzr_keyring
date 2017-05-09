import keyring


class KeyringCreds(object):

    def __init__(self):
        the_keyring = keyring.get_keyring()
        if hasattr(the_keyring, "appid"):
            the_keyring.appid = "Kibitzr"

    def __getitem__(self, key):
        return KeyringService(key)


class KeyringService(object):

    def __init__(self, service):
        self.service = service

    def __getitem__(self, key):
        return keyring.get_password(self.service, key)
