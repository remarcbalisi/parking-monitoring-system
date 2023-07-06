import sqlite3

conn = sqlite3.connect('parkme.db')


def create_vehicle_table():
    conn.execute('''CREATE TABLE vehicle
             (
             plate_number   VARCHAR(20)    NOT NULL UNIQUE,
             category   VARCHAR(50)    NOT NULL
             );''')
    print("Table created successfully")


def create_parking_space_table():
    conn.execute('''CREATE TABLE parking_space
             (
             parking_id   VARCHAR(20)    NOT NULL UNIQUE,
             parking_category   VARCHAR(50)    NOT NULL,
             initial_fee   FLOAT(8, 2)    NOT NULL,
             succeeding_fee   FLOAT(8, 2)    NOT NULL
             );''')
    print("Table created successfully")


def get_all_vehicles():
    cursor = conn.cursor()
    cursor.execute("SELECT plate_number, category from vehicle")
    vehicles = cursor.fetchall()
    for row in vehicles:
        print(row[0], row[1])

    cursor.close()
    return vehicles


def insert_new_vehicle(plate_number, category):
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO vehicle (plate_number, category) \
          VALUES ('{plate_number}', '{category}')")
    conn.commit()
    cursor.close()


def insert_new_parking_space(parking_id, parking_category, initial_fee, succeeding_fee):
    cursor = conn.cursor()
    sql_command = f"INSERT INTO parking_space (parking_id, parking_category, initial_fee, succeeding_fee) \
          VALUES ('{parking_id}', '{parking_category}', {initial_fee}, {succeeding_fee})"
    cursor.execute(sql_command)
    conn.commit()
    cursor.close()


def get_all_parking_spaces():
    cursor = conn.cursor()
    cursor.execute("SELECT * from parking_space")
    parking_spaces = cursor.fetchall()
    for row in parking_spaces:
        print(row[0], row[1])

    cursor.close()
    return parking_spaces


if __name__ == "__main__":
    pass
    # entry_name = 'Remarc'
    # entry_name2 = 'pawpaw'
    # message = f"Hello {entry_name}" + entry_name2
    # print(message)
    # message = 'hello {} {}'.format(entry_name, entry_name2)
    # print(message)
    # print(conn)
    # create_vehicle_table()
    # insert_new_vehicle('123-efg', '4-wheels')
    # get_all_vehicles()
    # create_parking_space_table()
    # insert_new_parking_space('parking-id-2', '2-wheels', succeeding_fee=30, initial_fee=100)
    get_all_parking_spaces()
