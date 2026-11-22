import sqlite3
import os

os.makedirs("data",exist_ok=True)
connection = sqlite3.connect(
    "/Users/kalyugwasi/Documents/GitHub/Practice/System_design/liveinteraction/data/video.db")
cursor = connection.cursor()

def initialize_db():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS guest (
            guest_id INTEGER PRIMARY KEY AUTOINCREMENT,
            guest_name TEXT NOT NULL
            );
        """)
    connection.commit()
    return f'Database for sessions initialized'

def add_guest(guest_name):
    cursor.execute("""
        INSERT INTO guest (guest_name)
        VALUES (guest_name);
    """,(guest_name,))
    connection.commit()
    return 'ADDED'

def del_guest(guest_name):
    cursor.execute("DELETE FROM guest WHERE guest_name = ?",(guest_name,))
    connection.commit()
    return cursor.rowcount > 0

def add_part(guest_id,video_id):
def remove_part(guest_id):
def change_vid(part_id,video_id):
def join_video():

initialize_db()