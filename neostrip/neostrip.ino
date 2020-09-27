#include <Adafruit_NeoPixel.h>
#include <fallpattern.h>
#include <julypattern.h>
#define PIN 6


Adafruit_NeoPixel strip = Adafruit_NeoPixel(90, PIN, NEO_GRB + NEO_KHZ800);
FallPattern fp(strip, 90, PIN);
JulyPattern jp(strip, 90, PIN);

void setup() {
  strip.begin();
  strip.setBrightness(255);
  strip.show();
  Serial.begin(9600);
}

void loop() {

  if (Serial.available() > 0) {
    // read the incoming byte:
    char incomingByte = Serial.read();
  
  switch(incomingByte) {
    case 'f': 
      fp.start();
    case 'j':
      jp.start();
    case 'z':
      strip.clear();
      strip.show();;
  }
  
  }
}
