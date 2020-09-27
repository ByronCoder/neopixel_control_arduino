#ifndef JulyPattern_h
#define JulyPattern_h

#include "Arduino.h"
#include <Adafruit_NeoPixel.h>

class JulyPattern
{
public:
    JulyPattern(Adafruit_NeoPixel strip, int num_pixels, int pin);
    void start();

private:
    Adafruit_NeoPixel _strip;
    int _num_pixels;
    int _pin;
    void colorWipe(uint32_t c, uint8_t wait);
    void theaterChase(uint32_t c, uint8_t wait);
    void julyPattern1();
    void julyPattern2();
};
#endif