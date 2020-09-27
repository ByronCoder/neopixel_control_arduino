#ifndef FallPattern_h
#define FallPattern_h

#include "Arduino.h"
#include <Adafruit_NeoPixel.h>

class FallPattern
{
public:
  FallPattern(Adafruit_NeoPixel strip, int num_pixels, int pin);
  void start();

private:
  Adafruit_NeoPixel _strip;
  int _num_pixels;
  int _pin;
  void colorWipe(uint32_t c, uint8_t wait);
  void theaterChase(uint32_t c, uint8_t wait);
  void fallPattern1();
  void fallPattern2();
};
#endif