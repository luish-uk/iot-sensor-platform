#include <dht_nonblocking.h>
#define DHT_SENSOR_TYPE DHT_TYPE_11

int maxVal = 300;
//The min is 0

static const int DHT_SENSOR_PIN = 2;
DHT_nonblocking dht_sensor(DHT_SENSOR_PIN, DHT_SENSOR_TYPE);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
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
  // put your main code here, to run repeatedly:
  float temperature; 
  float humidity; 
  int value = analogRead(A0);
  //Print to serial
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
