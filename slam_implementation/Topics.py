import sqlite3

def list_topics(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name FROM topics")
    topics = cursor.fetchall()

    conn.close()
    return topics

db_path = r"C:\Users\chopd\Downloads\my_pointcloud_data_0.db3"
topics = list_topics(db_path)

print("Topics in the database:")
for topic in topics:
    print(f"ID: {topic[0]}, Name: {topic[1]}")
