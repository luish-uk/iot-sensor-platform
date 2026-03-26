import sqlite3




def init_db():
    connect = sqlite3.connect("Sensor.db")
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS readings(id INTEGER PRIMARY KEY AUTOINCREMENT, sensor TEXT, value DOUBLE, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);""")
    connect.commit()
    connect.close()

def insert_reading(sensor_type, value):
    connect = sqlite3.connect("Sensor.db")
    cursor = connect.cursor()
    cmd = "INSERT INTO readings (sensor, value) VALUES (?, ?);"
    cursor.execute(cmd, (sensor_type, value))
    connect.commit()
    connect.close()

def get_readings():
    connect = sqlite3.connect("Sensor.db")
    cursor = connect.cursor()
    cursor.execute(f"SELECT * FROM readings;")
    results = cursor.fetchall()
    connect.close()
    return results

def limit_readings():
    connect = sqlite3.connect("Sensor.db")
    cursor = connect.cursor()
    cmd = "SELECT * FROM readings ORDER BY id DESC LIMIT 3;"
    cursor.execute(cmd)
    results = cursor.fetchall()
    connect.close()
    return results 

