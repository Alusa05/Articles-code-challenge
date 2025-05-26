from lib.db.connection import cursor

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

        @classmethod
        def find_by_author_id(cls, author_id):
            rows = cursor.execute("SELECT * FROM articles WHERE author_id = ?", (author_id,)).fetchall()
            return [cls(*row) for row in rows]
 