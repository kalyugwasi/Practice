import sqlite3
import os
os.makedirs("data",exist_ok=True)

connection = sqlite3.connect(
    "/Users/kalyugwasi/Documents/GitHub/Practice/System_design/ratelimiter/data/authorization.db"
)
connection.execute("PRAGMA foreign_keys = ON;")
cursor = connection.cursor()
def initialize_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tiers (
        tier_id INTEGER PRIMARY KEY,
        tier_name TEXT NOT NULL,
        rpm INTEGER NOT NULL
        );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clients (
        client_id TEXT PRIMARY KEY,
        tier_id INTEGER,
        is_authorized BOOLEAN NOT NULL,
        FOREIGN KEY (tier_id) REFERENCES tiers (tier_id)
        );
    """)

    tiers_data = [
        (1,"Guest",60),
        (2,"Basic",120),
        (3,"Pro",180)
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO tiers (tier_id, tier_name, rpm)
        VALUES (?,?,?);
    """, tiers_data)

    clients_data = [
        ("A",1,True),
        ("B",1,True),
        ("C",1,True)
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO clients (client_id,tier_id,is_authorized)
        VALUES (?,?,?);
    """,clients_data)

    connection.commit()
    print("Database initialized and seeded successfully.")

def get_client(client_name):
    cursor.execute("""
        SELECT c.client_id, c.is_authorized, t.tier_name, t.rpm
        FROM clients c
        LEFT JOIN tiers t ON c.tier_id = t.tier_id
        WHERE c.client_id = ?;
    """,(client_name,))
    row = cursor.fetchone()
    if row:
        return {
            "client_id": row[0],
            "is_authorized": row[1],
            "tier_name": row[2],
            "rpm": row[3]
        }
    return None

def add_client(client_name,tier_id=1,is_authorized=True):
    try:
        cursor.execute("""
            INSERT INTO clients (client_id,tier_id,is_authorized)
            VALUES (?,?,?);
        """, (client_name,tier_id,is_authorized))
        connection.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def del_client(client_name):
    cursor.execute("DELETE FROM clients WHERE client_id = ?;", (client_name,))
    connection.commit()
    return cursor.rowcount > 0

initialize_db()

'''
print(get_client("A"))
print(check_auth("A"))
print(check_auth("UNKNOWN"))
print(add_client("D", 2, True))
print(get_client("D"))
print(del_client("D"))
'''