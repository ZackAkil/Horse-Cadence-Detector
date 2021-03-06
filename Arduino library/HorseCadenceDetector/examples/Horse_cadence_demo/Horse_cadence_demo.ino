/*
  Analog input, analog output, serial output

 Reads an analog input pin, maps the result to a range from 0 to 255
 and uses the result to set the pulsewidth modulation (PWM) of an output pin.
 Also prints the results to the serial monitor.

 The circuit:
 * potentiometer connected to analog pin 0.
   Center pin of the potentiometer goes to the analog pin.
   side pins of the potentiometer go to +5V and ground
 * LED connected from digital pin 9 to ground

 created 29 Dec. 2008
 modified 9 Apr 2012
 by Tom Igoe

 This example code is in the public domain.

 */
 
 #include <HorseCadenceDetector.h>

HorseCadenceDetector hcd;

// These constants won't change.  They're used to give names
// to the pins used:
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
const int analogOutPin = 9; // Analog output pin that the LED is attached to

int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
}

void loop() {
  
  // read sensor
  sensorValue = analogRead(analogInPin);
  // scaling values for my specific sensor (NOT NEEDED)
  outputValue = map(sensorValue, 0, 1023, 0, 255);
  unsigned int scal = map(outputValue, 100, 160, 700, 11000);
  
  // feed sensor data as often as possible 
  hcd.FeedData(scal);
  
  // fetch value whenever you want
  Serial.println(hcd.GetCurrentCadence());

}
