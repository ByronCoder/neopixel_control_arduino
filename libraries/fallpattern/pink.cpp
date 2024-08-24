#include <Arduino.h>
#include <pink.h>
#include <Adafruit_NeoPixel.h>

pink::pink(Adafruit_NeoPixel strip, int num_pixels, int pin)
{
    _strip = strip;
    _num_pixels = num_pixels;
    _pin = pin;
}

void pink::start()
{
    while (true)
    {
        if (Serial.available() > 0)
        {
            break;
        }

        colorWipe(_strip.Color(255, 0, 255), 255); // pink
    }
}

void pink::colorWipe(uint32_t c, uint8_t wait)
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
