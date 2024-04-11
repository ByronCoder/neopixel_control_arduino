#include <Arduino.h>
#include <alertpattern.h>
#include <Adafruit_NeoPixel.h>

AlertPattern::AlertPattern(Adafruit_NeoPixel strip, int num_pixels, int pin)
{
    _strip = strip;
    _num_pixels = num_pixels;
    _pin = pin;
}

void AlertPattern::start()
{
    while (true)
    {
        if (Serial.available() > 0)
        {
            break;
        }

        colorWipe(_strip.Color(255, 0, 255), 50); // Red
    }
}

void AlertPattern::colorWipe(uint32_t c, uint8_t wait)
{
    for (uint16_t i = 0; i < _strip.numPixels(); i++)
    {
        if (Serial.available() > 0)
        {

            break;
        }

        _strip.setPixelColor(i, c);
        _strip.show();
        delay(wait);
    }
}
