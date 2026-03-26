import sqlite3
con = sqlite3.connect("Database.db")

cur = con.cursor()

cur.execute("CREATE TABLE Light_Sensor(percent int)")
