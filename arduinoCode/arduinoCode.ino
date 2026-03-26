#include <dht_nonblocking.h> //Library for dht_11 from ELEGOO
#define DHT_SENSOR_TYPE DHT_TYPE_11 

static const int DHT_SENSOR_PIN = 2; // Assign's pin 2 to the temperature sensor 
DHT_nonblocking dht_sensor(DHT_SENSOR_PIN, DHT_SENSOR_TYPE);

void setup() {
  Serial.begin(9600); //Initialize serial monitor 
}

//Update temperature every 3 seconds 
static bool measure_environment(float *temperature, float *humidity)
{
  static unsigned long measurement_timestamp = millis();

  if (millis() - measurement_timestamp > 3000ul)
  {
    if (dht_sensor.measure(temperature, humidity))
    {
      measurement_timestamp = millis();
      return true;
    }
  }
  return false;
}


void loop() {
  //Initilize variables
  float temperature; 
  float humidity; 
  //Collect pin data for photoresister (light sensor)
  int value = analogRead(A0);
  //Print to serial from the photoresistor and DHT11 in JSON format
  if (measure_environment(&temperature, &humidity))
  {
    Serial.print("{");
    Serial.print("\"Temp (Celsius)\":");
    Serial.print(temperature, 1);
    Serial.print(",");
    Serial.print("\"Humidity (%)\":");
    Serial.print(humidity, 1);
    Serial.print(",");
    Serial.print("\"Light\":");
    Serial.print(value);
    Serial.println("}");
  
  delay(500);
  }
}
