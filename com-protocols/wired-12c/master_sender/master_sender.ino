#include <Wire.h>

void setup() {
  Wire.begin();        // Initialize I2C communication
  Serial.begin(9600);  // Initialize serial communication
}

void loop() {
  if (Serial.available() > 0) { 
    String input = Serial.readStringUntil("\n"); 
    Wire.beginTransmission(9);    
    Wire.write(input.c_str());    // Convert the String to a C-style string and send over I2C
    Wire.endTransmission();         
    delay(1000);                 
  }
}
