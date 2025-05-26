from .connection import conn, cursor

def seed_db():
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    cursor.execute("DELETE FROM articles")

    cursor.execute("INSERT INTO authors (name, email) VALUES (?,?)", ("Alice", "alice@email.com"))
    cursor.execute("INSERT INTO authors (name, email) VALUES (?,?)", ("Bob", "bob@email.com"))

    cursor.execute("INSERT INTO magazines (title, category) VALUES (?, ?)", ("Tech Weekly", "Technology"))
    cursor.execute("INSERT INTO magazines (title, category) VALUES (?, ?)", ("Health Monthly", "Health"))

    cursor.execute("INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)",
                   ("AI Trends", "Latest trends in AI...", 1, 1))
    cursor.execute("INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)",
                   ("Healthy Eating", "Tips for a better diet", 2, 2))

    conn.commit()