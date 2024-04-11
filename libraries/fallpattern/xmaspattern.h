#ifndef XmasPattern_h
#define XmasPattern_h

#include "Arduino.h"
#include <Adafruit_NeoPixel.h>

class XmasPattern
{
public:
  XmasPattern(Adafruit_NeoPixel strip, int num_pixels, int pin);
  void start();

private:
  Adafruit_NeoPixel _strip;
  int _num_pixels;
  int _pin;

  void CandyCane (int sets, int width, int wait);
  void RandomWhite (int sets, int wait);
  void RandomColor(int sets, int wait);
  void RainbowStripe(int sets, int width, int wait);
  void colorWipe(uint32_t c, uint8_t wait);
  void rainbowCycle(uint8_t sets, uint8_t wait);
  uint32_t Wheel(byte WheelPos);
  void alternateColor(uint32_t cl, uint32_t c2, uint8_t wait);
  void randomColorFill(uint8_t wait);
  void randomPositionFill(uint32_t c, uint8_t wait);
  void middleFill(uint32_t c, uint8_t wait);
  void sideFill(uint32_t c, uint8_t wait);
  
  
};
#endif