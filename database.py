import sqlite3




def init_db():
    """
    Initilizes database if it does not already exist
    """

    connect = sqlite3.connect("Sensor.db")
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS readings(id INTEGER PRIMARY KEY AUTOINCREMENT, sensor TEXT, value DOUBLE, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);""")
    connect.commit()
    connect.close()

def insert_reading(sensor_type, value):
    """
    Inserts readings into the SQL database.
    Args: 
        sensor_type (str): Type of sensor (example photoresistor would be light sensor, DHT11 sensor would be a temperature sensor)
        value (int): value of the sensor from the serial monitor
    """

    connect = sqlite3.connect("Sensor.db")
    cursor = connect.cursor()
    cmd = "INSERT INTO readings (sensor, value) VALUES (?, ?);"
    cursor.execute(cmd, (sensor_type, value))
    connect.commit()
    connect.close()

def get_readings():
    """
    Return's readings from the SQL Database using query statements 
    """

    connect = sqlite3.connect("Sensor.db")
    cursor = connect.cursor()
    cursor.execute(f"SELECT * FROM readings;")
    results = cursor.fetchall()
    connect.close()
    return results

def limit_readings():
    """
    Return's only one reading from each device (each sensor is in a seperate row assuming all 3 are used), this is to be displayed on the flask server.  
    """
    connect = sqlite3.connect("Sensor.db")
    cursor = connect.cursor()
    cmd = "SELECT * FROM readings ORDER BY id DESC LIMIT 3;"
    cursor.execute(cmd)
    results = cursor.fetchall()
    connect.close()
    return results 

