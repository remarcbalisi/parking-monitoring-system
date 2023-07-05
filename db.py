import sqlite3

conn = sqlite3.connect('parkme.db')


def create_vehicle_table():
    conn.execute('''CREATE TABLE vehicle
             (
             plate_number   VARCHAR(20)    NOT NULL UNIQUE,
             category   VARCHAR(50)    NOT NULL
             );''')
    print("Table created successfully")


def get_all_vehicles():
    cursor = conn.cursor()
    cursor.execute("SELECT plate_number, category from vehicle")
    for row in cursor.fetchall():
        print(row[0], row[1])

    cursor.close()
    return cursor.fetchall()


def insert_new_vehicle(plate_number, category):
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO vehicle (plate_number, category) \
          VALUES ('{plate_number}', '{category}')")
    conn.commit()
    cursor.close()


if __name__ == "__main__":
    pass
    # print(conn)
    # create_vehicle_table()
    # insert_new_vehicle('123-efg', '4-wheels')
    get_all_vehicles()
