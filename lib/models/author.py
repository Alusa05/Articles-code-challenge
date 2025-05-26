from lib.db.connection import cursor

class Author:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

        @classmethod
        def all(cls):
            rows = cursor.execute("SELECT * FROM authors").fetchall()
            return [cls(*row) for row in rows]
        
        def articles(self):
            from .article import Article
            return Article.find_by_author(self.id)
        
        def magazines(self):
            from .magazine import Magazine
            return Magazine.find_by_author(self.id)