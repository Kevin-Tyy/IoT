#include <Wire.h>

#define BUFFER_SIZE 64 // Maximum size of the received message

char receivedMessage[BUFFER_SIZE]; // Buffer to store the received message
int messageIndex = 0; // Index to keep track of the current position in the buffer

void setup() {
  Wire.begin(9); // Address for Arduino2
  Wire.onReceive(receiveEvent);
  Serial.begin(9600);
}

void loop() {
  // Additional code can be added here
}

void receiveEvent(int numBytes) {
  if (numBytes <= BUFFER_SIZE) { // Check if the received message fits in the buffer
    while (Wire.available()) {
      receivedMessage[messageIndex++] = Wire.read(); // Read the received byte and store it in the buffer
    }
    receivedMessage[messageIndex] = '\0'; // Null-terminate the message to turn it into a string
    Serial.print("Received data from Arduino1: ");
    Serial.println(receivedMessage); // Print out the received message
    messageIndex = 0; // Reset the message index for the next message
  } else {
    // If the received message is too large, handle the error accordingly
    Serial.println("Error: Received message exceeds buffer size");
    while (Wire.available()) {
      Wire.read(); // Read and discard the remaining bytes from the buffer
    }
    messageIndex = 0; // Reset the message index to prepare for the next message
  }
}