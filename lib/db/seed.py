from .connection import conn, cursor

def seed_db():
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    cursor.execute("DELETE FROM articles")

    cursor.execute("INSERT INTO authors (name, email) VALUES (?,?)", ("Alice", "alice@email.com"))
    cursor.execute("INSERT INTO authors (name, email) VALUES (?,?)", ("Bob", "bob@email.com"))
    