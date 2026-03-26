from flask import Flask, render_template
import serial 
from database import init_db, insert_reading, get_readings
import json

app = Flask(__name__)

ser = serial.Serial('/dev/ttyACM0', 9600)

init_db()

data = ser.readline().decode().strip()

@app.route("/")
def home():
    data_dict = json.loads(data)
    light_percent = data_dict["light"]

    insert_reading(light_percent)
    readings = get_readings()
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