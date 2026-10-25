import sqlite3
import os

os.makedirs(name="data",exist_ok=True)
connection= sqlite3.connect(
    "/Users/kalyugwasi/Documents/GitHub/Practice/System_design/ratelimiter/data/reply.db"
)
cursor = connection.cursor()
def initialize_db():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS response (
            client_id TEXT PRIMARY KEY,
            hits INTEGER NOT NULL
            );
    """)
    connection.commit()
    print("Response handling started")

def get_hits(client_name):
    cursor.execute("""
        SELECT r.client_id, r.hits
        FROM response r
        WHERE client_id = ?;
    """,(client_name,))
    row = cursor.fetchone()
    if row:
        return row[1]
    else:
        return 0

def add_client(client_name):
    try:
        cursor.execute("""
            INSERT INTO response (client_id, hits)
            VALUES (?, 1)
            ON CONFLICT(client_id)
            DO UPDATE SET hits = hits + 1;
        """,(client_name,))
        connection.commit()
        return True
    except sqlite3.IntegrityError:
        return False

initialize_db()