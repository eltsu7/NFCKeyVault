from sqlitedict import SqliteDict

class Database:

    def __init__(self, db_name):
        self.db = SqliteDict(db_name)

    def add_key_to_db(self, new_key):
        keys = self.db["keys"]["keys"]
        keys.append(new_key)
        self.db["keys"] = {"keys": keys}
        self.db.commit()

    def is_key_in_db(self, key):
        try:
            return key in self.db["keys"]["keys"]
        except KeyError:
            return False
