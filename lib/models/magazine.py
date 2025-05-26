from lib.db.connection import cursor

class Magazine:
    def __init__(self, id, title, category):
        self.id = id
        self.title = title
        self.category = category

        @class
