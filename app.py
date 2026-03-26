from flask import Flask, render_template
import serial 
from database import init_db, insert_reading, get_readings, limit_readings
import json

app = Flask(__name__)

ser = serial.Serial('/dev/ttyACM0', 9600)

init_db()

@app.route("/")
def home():
    data = ser.readline().decode().strip()
    data_dict = json.loads(data)
    light = data_dict["Light"]
    Temp = data_dict["Temp (Celsius)"]
    Humidity = data_dict["Humidity (%)"]
    insert_reading("temperature", Temp)
    insert_reading("humidity", Humidity)
    insert_reading("light", light)

    readings = limit_readings()

#OUTPUT: [(384, 'light', 137.0, '2026-03-26 12:22:29'), (383, 'humidity', 39.0, '2026-03-26 12:22:29'), (382, 'temperature', 22.0, '2026-03-26 12:22:29')]

    return render_template('index.html', readings=readings)

app.run(host="0.0.0.0", port=5000)
# class Data:
#     def insert(self, column):
#         line = "INSERT INTO {column} VALUES({self.lightData})"
#         return line
#     def query(self, column=None, table=None):
#         if table == None:
#             table = "sqlite_master"
#         if column == None:
#             column = "*"
#         else:
#             columns = ""
#             l = len(column)
#             for i in range(l-2):
#                 columns += f'{column[i]}, '
#             columns += f'{column[-1]}'
#         line = "SELECT {column}"