from Crypto.Hash import SHA256 as hashFunction
import datetime as date


class Block:
    def __init__(self, transaction=None, parent_hash=None, height=0, timestamp = '31 Aug 2018 11:00:00'):
        self.height = height
        self.timestamp = timestamp
        self.transaction = transaction
        self.parent_hash = parent_hash
        self.hash = self.hash_self()

    def hash_self(self):
        hash = hashFunction.new()
        hash.update((str(self.height) + 
                    str(self.timestamp) + 
                    str(self.transaction) + 
                    str(self.parent_hash)).encode())
        return hash.hexdigest()