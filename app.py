from flask import Flask, render_template
import serial 
from database import init_db, insert_reading, get_readings, limit_readings
import json

app = Flask(__name__)

ser = serial.Serial('/dev/ttyACM0', 9600)

init_db()

@app.route("/")
def home():
    """
    Default home page functionality
    Actions:
        - Reads the Arduino Data from the serial monitor that's JSON fomatted 
        - Seperates each of the values to their respective variables 
        - Log's values to database 
        - Collect's the last 3 reading's of those values form the database 
        - Prints it to the home page 
    """
    data = ser.readline().decode().strip()
    data_dict = json.loads(data)
    light = data_dict["Light"]
    Temp = data_dict["Temp (Celsius)"]
    Humidity = data_dict["Humidity (%)"]
    insert_reading("temperature", Temp)
    insert_reading("humidity", Humidity)
    insert_reading("light", light)

    readings = limit_readings()

    return render_template('index.html', readings=readings)

app.run(host="0.0.0.0", port=5000)