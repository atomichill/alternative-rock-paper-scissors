import secrets

class Key:
    def __init__(self, bts) -> None:
        self.byte_size = bts

    def generate_key(self):
        secret_key = secrets.token_bytes(self.byte_size)
        return secret_key