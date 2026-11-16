import numpy as np
import sqlite3
import matplotlib.pyplot as plt
import struct

class SimpleSLAM:
    def __init__(self):
        self.map = np.zeros((500, 500), dtype=np.uint8)
        self.position = (250, 250)

    def update(self, sensor_data):
        x, y = self.position
        for angle, distance in sensor_data:
            dx = int(distance * np.cos(angle))
            dy = int(distance * np.sin(angle))
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < self.map.shape[1] and 0 <= new_y < self.map.shape[0]:
                self.map[new_y, new_x] = 255

    def show_map(self):
        plt.imshow(self.map, cmap='gray')
        plt.title('SLAM Map')
        plt.show()

def get_topic_id(db_path, topic_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM topics WHERE name=?", (topic_name,))
    topic_id = cursor.fetchone()

    conn.close()
    return topic_id[0] if topic_id else None

def fetch_sensor_data(db_path, topic_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT data FROM messages WHERE topic_id=?", (topic_id,))
    data = cursor.fetchall()

    sensor_data_list = []
    for row in data:
        blob_data = row[0]
        sensor_data = []
        for i in range(0, len(blob_data), 16):
            angle, distance = struct.unpack('dd', blob_data[i:i+16])
            sensor_data.append((angle, distance))
        sensor_data_list.append(sensor_data)

    conn.close()
    return sensor_data_list

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

topic_name = '/rslidar_points'
topic_id = get_topic_id(db_path, topic_name)
if topic_id is None:
    print(f"Topic '{topic_name}' not found in the database.")
else:
    sensor_data_list = fetch_sensor_data(db_path, topic_id)

    slam = SimpleSLAM()
    for sensor_data in sensor_data_list:
        slam.update(sensor_data)

    slam.show_map()