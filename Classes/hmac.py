import hmac
import hashlib

class Hmac():
    def __init__(self, key, message) -> None:
        self.msg = message
        self.keys = key

    def calc_hmac(self):
        imported_message = bytes(self.msg, 'utf-8')
        dig = hmac.new(self.keys, imported_message, hashlib.sha3_256).hexdigest().upper()
        return dig

