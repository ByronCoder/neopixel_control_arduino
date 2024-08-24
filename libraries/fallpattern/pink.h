#ifndef pink_h
#define pink_h

#include "Arduino.h"
#include <Adafruit_NeoPixel.h>

class pink
{
public:
    pink(Adafruit_NeoPixel strip, int num_pixels, int pin);
    void start();

private:
    Adafruit_NeoPixel _strip;
    int _num_pixels;
    int _pin;
    void colorWipe(uint32_t c, uint8_t wait);
};
#endif