// Arduino UNO On Arduino IDE

#include <Wire.h>

const int potPin = A0;
int potValue = 0;

void setup() {
  Wire.begin(8); 
  Wire.onRequest(sendData);
  Serial.begin(9600);
}

void loop() {
  potValue = analogRead(potPin);
  delay(100); 
}

void sendData() {
  Wire.write(potValue >> 8);    // High byte
  Wire.write(potValue & 0xFF);  // Low byte
}
