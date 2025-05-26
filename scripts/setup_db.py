from lib.db.connection import conn, cursor
from lib.db.seed import seed_db

with open("lib/db/schema.sql") as f:
    cursor.executescript(f.read())
    conn.commit()

    seed_db()
    print("Database setup complete with schema and seeded data.")