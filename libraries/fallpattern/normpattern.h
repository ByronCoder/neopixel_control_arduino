#ifndef NormPattern_h
#define NormPattern_h

#include "Arduino.h"
#include <Adafruit_NeoPixel.h>

class NormPattern
{
public:
    NormPattern(Adafruit_NeoPixel strip, int num_pixels, int pin);
    void start();

private:
    Adafruit_NeoPixel _strip;
    int _num_pixels;
    int _pin;
    void colorWipe(uint32_t c, uint8_t wait);
    void theaterChase(uint32_t color, uint8_t wait);
    void rainbow(int wait);
    void theaterChaseRainbow(int wait);
};
#endif