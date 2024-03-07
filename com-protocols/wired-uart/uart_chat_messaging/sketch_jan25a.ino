#include <SoftwareSerial.h>
SoftwareSerial mySerial(2, 3);
void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
}
void loop() {
  if (mySerial.available()) {
    String receivedMessage = mySerial.readStringUntil('\n');
    Serial.println("Hugues: " + receivedMessage);
  }
  if (Serial.available()) {
    String userInput = Serial.readStringUntil('\n');
    mySerial.println(userInput);
    Serial.println("Kevin: " + userInput);
  }
}