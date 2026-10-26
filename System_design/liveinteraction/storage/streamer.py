import sqlite3
import os

os.makedirs(name="data", exist_ok=True)
connection = sqlite3.connect(
    "/Users/kalyugwasi/Documents/GitHub/Practice/System_design/liveinteraction/data/video.db"
)
cursor = connection.cursor()


def initialize_db():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS videos (
            video_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            status TEXT NOT NULL
            );
        """)
    connection.commit()
    print("Video Database initialized")


def check_stream(video_id):
    cursor.execute(
        """
        SELECT v.video_id
        FROM videos v
        WHERE v.video_id = ?;
    """,
        (video_id,),
    )
    row = cursor.fetchone()
    if row:
        return True
    return False


def create_stream(user_id):
    cursor.execute(
        """
        INSERT INTO videos (user_id,status)
        VALUES (?,?)
        RETURNING format('VID=%5d',video_id)
    """,
        (user_id, "live"),
    )
    res = cursor.fetchone()
    connection.commit()
    if res:
        return f"Stream created successfully by video id: {res[0]}"
    return f"Failed to create the stream"


def update_stream_status(video_id):
    cursor.execute(
        """
        UPDATE videos
        SET status = "Not_Live"
        WHERE video_id = ?
    """,
        (video_id,),
    )
    connection.commit()
    return f"Field updated."


def del_stream(video_id):
    cursor.execute("DELETE FROM videos WHERE video_id = ?", (video_id,))
    connection.commit()
    return cursor.rowcount > 0


initialize_db()
'''
print(create_stream(1))
print(check_stream(1))
print(update_stream_status(1))
print(del_stream(1))
print(check_stream(1))
'''