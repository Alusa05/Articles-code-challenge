from lib.db.connection import cursor

class Magazine:
    def __init__(self, id, title, category):
        self.id = id
        self.title = title
        self.category = category

        @classmethod
        def find_by_author_id(cls, author_id):
            rows = cursor.execute("""
                                  SELECT DISTINCT m.* FROM magazines m
                                  JOIN articles a ON m.id = a.magazine_id
                                  where a.author_id = ?
                                  """,(author_id)).fetchall()
            return [cls(*row) for row in rows]
