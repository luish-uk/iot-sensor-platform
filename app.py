from flask import Flask, render_template
import serial 


app = Flask(__name__)
ser = serial.Serial('/dev/ttyACM0', 9600)

data = ser.readline().decode().strip()

@app.route("/")
def home():
    data = ser.readline().decode().strip()
    percent = data
    percent = percent["light"]
    return render_template('index.html', brightness = percent)

app.run(host="0.0.0.0", port=5000)
class Data:
    def __init__(self):
        self.lightData = data
        return self.data
    
    def insert(self, column):
        line = "INSERT INTO {column} VALUES({self.lightData})"
        return line
    def query(self, column=None, table=None):
        if table == None:
            table = "sqlite_master"
        if column == None:
            column = "*"
        else:
            columns = ""
            l = len(column)
            for i in range(l-2):
                columns += f'{column[i]}, '
            columns += f'{column[-1]}'
        line = "SELECT {column}"