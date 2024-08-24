#include <Adafruit_NeoPixel.h>
#include <normpattern.h>
#include <fallpattern.h>
#include <julypattern.h>
#include <xmaspattern.h>
#include <alertpattern.h>
#include <blue.h>
#include <red.h>
#include <pink.h>
#define PIN 6

Adafruit_NeoPixel strip = Adafruit_NeoPixel(90, PIN, NEO_GRB + NEO_KHZ800);
NormPattern np(strip, 90, PIN);
JulyPattern jp(strip, 90, PIN);
FallPattern fp(strip, 90, PIN);
XmasPattern cp(strip, 90, PIN);
AlertPattern ap(strip, 90, PIN);
blue bl(strip, 90, PIN);
red re(strip, 90, PIN);
pink pi(strip, 90, PIN);

void setup()                                                                                                                                                                          
{
  strip.begin();
  strip.setBrightness(255);
  strip.show();
  Serial.begin(9600);
}

void loop()
{

  if (Serial.available() > 0)
  {
    // read the incoming byte:
    char incomingByte = Serial.read();

    switch (incomingByte)
    {
    case 'n':
      np.start();
    case 'j':
      jp.start();
    case 'f':
      fp.start();
    case 'c':
      cp.start();
    case 'a':
      ap.start();
    case 'p':
      pi.start();
    case 'b':
      bl.start();
    case 'r':
      re.start();
    case 'z':
      strip.clear();
      strip.show();
    }
  }
}
