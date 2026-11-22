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


def check_stream(video_id,req):
    cursor.execute(
        """
        SELECT v.video_id,v.status
        FROM videos v
        WHERE v.video_id = ?;
    """,
        (video_id,),
    )
    row = cursor.fetchone()
    if not row:
        return f"Video Id doesn't exist"
    if req == "v":
        return True
    return row[1]


def create_stream(user_id):
    cursor.execute(
        """
        INSERT INTO videos (user_id,status)
        VALUES (?,?)
        RETURNING video_id
    """,
        (user_id, "live"),
    )
    res = cursor.fetchone()
    connection.commit()
    if not res:
        return f"Failed to create the stream"
    return f"Stream created successfully by video id: {res[0]}"


def update_stream_status(video_id):
    cursor.execute(
        """
        UPDATE videos
        SET status = "Ended"
        WHERE video_id = ?
    """,
        (video_id,),
    )
    connection.commit()
    return cursor.rowcount > 0


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