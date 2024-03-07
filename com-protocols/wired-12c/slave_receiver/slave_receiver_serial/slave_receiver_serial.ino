#include <Wire.h>

void setup() {
  Wire.begin(9);
  Wire.onReceive(receiveEvent);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

}

void receiveEvent(){
   Serial.print("Received MSG: ");
  while (Wire.available()) {
    char receivedChar = Wire.read();
    Serial.print(receivedChar);
  }
  Serial.println();
}