import sqlite3


def get_connection():
    conn = sqlite3.connect('parkme.db')
    return conn


def create_vehicle_table():
    get_connection().execute('''CREATE TABLE vehicle
             (
             plate_number   VARCHAR(20)    NOT NULL UNIQUE,
             category   VARCHAR(50)    NOT NULL
             );''')
    print("Table created successfully")


def get_all_vehicles():
    cursor = get_connection().cursor()
    cursor.execute("SELECT plate_number, category from vehicle")
    for row in cursor.fetchall():
        print("PLATE NUMBER = ", row[0])
        print("CATEGORY = ", row[1], "\n")

    cursor.close()


def insert_new_vehicle(plate_number, category):
    cursor = get_connection().cursor()
    cursor.execute(f"INSERT INTO vehicle (plate_number, category) \
          VALUES ('{plate_number}', '{category}')")
    get_connection().commit()
    cursor.close()


if __name__ == "__main__":
    pass
    # print(get_connection())
    # create_vehicle_table()
    # insert_new_vehicle('123-abc', '4-wheels')
    get_all_vehicles()
