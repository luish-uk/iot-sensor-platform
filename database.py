import sqlite3




def init_db():
    connect = sqlite3.connect("Sensor.db")
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS readings(id INTEGER PRIMARY KEY AUTOINCREMENT, light_percent INT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);""")
    connect.commit()
    connect.close()

def insert_reading(light_percent):
    connect = sqlite3.connect("Sensor.db")
    cursor = connect.cursor()
    cursor.execute(f"INSERT INTO readings (light_percent) VALUES ({light_percent});")
    connect.commit()
    connect.close()

def get_readings():
    connect = sqlite3.connect("Sensor.db")
    cursor = connect.cursor()
    cursor.execute(f"SELECT * FROM readings;")
    results = cursor.fetchall()
    connect.close()
    return results
