# iot-sensor-platform
## Whay does this project do? 
This project collects data from the arduino photoresistor and the DHT11 sensor both connected to a breadboard to detect a room's brightness and it's temperature + humidity respectively. This code requires these elements along with the necessary wiring mentioned later on to work. 

The readings are then input into python file reading the arduino's serial monitor and takes the values to insert them into an SQLite3 database. This database stores all the values from the sensor which are then returned back to the app file to be pushed onto the flask web server. Once on the webserver it will display the current room's temperature, as well as it's humidity and brightness, it's formatted into a html table and displayed using jinja. The values can be updated through each reload of the website 


## Hardware Requirements 
- Arduino Uno 
- DHT11 Temperature and Humidity Sensor 
- Light Sensor 
  - M/M Jumper wires + breadboard 
  or 
  - M/F Jumper wires 
- A USB Cable connecting the Arduino to a computer 

## Software / Technologies Used 
- Python (Flask, SQLite, PySerial)
- Arduino C++
- HTML/CSS 

## How to run it 
### Wiring diagram
![image](https://image2url.com/r2/default/images/1774544315674-d0ad45c0-d451-4444-a7b2-cdc01d253150.png)

## Code 
Once the arduino is connected to your computer, run the arduino code in the arduino IDE, then run the app.py file, your terminal should output the flask URL and from there you can view the web interface. 

## Features 
- Real-time sensor readings 
- Database storage of all recordings 
- Web interface displaying data in table format 
- Tracks temperature humidity and light levels 

## What I Learned
I learned how to implement an iot device data from it's serial code to a Python script then to an SQLite server and then to a web dashboard. All while using a python framework for the front end and backend + the C++ code for the arduino. I learned how to search for values in a database as well as how databases can be useful for providing specific information with their powerful query's as well as helpful for storing many values. Even down to the wiring and understanding where things go where all first times for me. 

## Code statistics 
- 36 lines in app.py
- 54 lines in database.py
- 50 lines in arduinoCode.ino
- 30 lines in index.html
- 21 lines in styles.css
Total: 191 lines