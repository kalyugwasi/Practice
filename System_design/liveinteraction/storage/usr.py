import sqlite3
import os

os.makedirs(name="data",exist_ok=True)

connection = sqlite3.connect(
    '/Users/kalyugwasi/Documents/GitHub/Practice/System_design/liveinteraction/data/auth.db'
)
cursor = connection.cursor()
def initialize_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        user_name TEXT
        );
    """)
    connection.commit()
    print("DataBase initialized")

def add_user(user_id,user_name):
    try:
        cursor.execute("""
            INSERT INTO users (user_id,user_name)
            VALUES (?,?);
        """,(user_id,user_name))
        connection.commit()
        return True
    except sqlite3.IntegrityError:
        return False
def check_user(user_id):
    cursor.execute("""
        SELECT u.user_id
        FROM users u
        WHERE u.user_id = ?;
    """,(user_id,))
    row = cursor.fetchone()
    if row:
        return True
    return None

def del_user(user_id):
    cursor.execute("DELETE FROM users WHERE user_id = ?;",(user_id,))
    connection.commit()
    return cursor.rowcount > 0
initialize_db()

print(add_usr(1,"aman"))
print(chk_usr(1))
print(del_user(1))
print(chk_usr(1))