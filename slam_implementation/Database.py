import sqlite3

def examine_db_structure(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:")
    for table in tables:
        print(table[0])
        cursor.execute(f"PRAGMA table_info({table[0]})")
        columns = cursor.fetchall()
        print("Columns in the table:")
        for column in columns:
            print(column[1], column[2])

    conn.close()

db_path = r"C:\Users\chopd\Downloads\my_pointcloud_data_0.db3"
examine_db_structure(db_path)