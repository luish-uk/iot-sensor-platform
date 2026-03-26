
int maxVal = 300;
//The min is 0

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int value = analogRead(A0);
  int percent = value * 100 / maxVal;
  percent = 100 - percent;
  //Print to serial
  Serial.print("{\"light\":");
  Serial.print(percent);
  Serial.println("}");
  
  delay(500);
}
