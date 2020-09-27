#include <Arduino.h>
#include <julypattern.h>
#include <Adafruit_NeoPixel.h>

JulyPattern::JulyPattern(Adafruit_NeoPixel strip, int num_pixels, int pin)
{
    _strip = strip;
    _num_pixels = num_pixels;
    _pin = pin;
}

void JulyPattern::start()
{
    while (true)
    {
        if (Serial.available() > 0)
        {
            break;
        }

        colorWipe(_strip.Color(255, 0, 0), 50);     // Red
        colorWipe(_strip.Color(255, 255, 255), 50); // White
        colorWipe(_strip.Color(0, 0, 255), 50);     // Blue

        theaterChase(_strip.Color(255, 255, 255), 50); // White
        theaterChase(_strip.Color(255, 0, 0), 50);     // Red
        theaterChase(_strip.Color(0, 0, 255), 50);     // Blue

        julyPattern1();
        julyPattern2();
    }
}

void JulyPattern::colorWipe(uint32_t c, uint8_t wait)
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

void JulyPattern::theaterChase(uint32_t c, uint8_t wait)
{

    for (int j = 0; j < 10; j++)
    {
        if (Serial.available() > 0)
        {

            break;
        }

        //do 10 cycles of chasing
        for (int q = 0; q < 3; q++)
        {
            for (int i = 0; i < _strip.numPixels(); i = i + 3)
            {
                _strip.setPixelColor(i + q, c); //turn every third pixel on
            }
            _strip.show();

            delay(wait);

            for (int i = 0; i < _strip.numPixels(); i = i + 3)
            {
                _strip.setPixelColor(i + q, 0); //turn every third pixel off
            }
        }
    }
}

void JulyPattern::julyPattern1()
{
    // 0 - Red
    // 1 - Blue
    // 2 - White
    // 3 - Red
    // 4 - Blue
    // 5 - White
    // 6 - Red
    // 7 - Blue
    // 8 - White

    int r = 0;
    int b = 1;
    int w = 2;

    for (int i = 0; i < _strip.numPixels(); i++)
    {
        if (Serial.available() > 0)
        {

            break;
        }

        // set red pixels
        _strip.setPixelColor(r, 255, 0, 0);
        r = r + 3;
        //  delay(50);
        _strip.show();
        // set blue pixels
        _strip.setPixelColor(b, 0, 0, 255);
        b = b + 3;
        // delay(50);
        _strip.show();
        // set blue pixels
        _strip.setPixelColor(w, 255, 255, 255);
        w = w + 3;
        // delay(50);
        _strip.show();

        delay(50);
    }
}

void JulyPattern::julyPattern2()
{
    for (int i = 0; i < 1000; i++)
    {
        if (Serial.available() > 0)
        {

            break;
        }

        _strip.setPixelColor(random(0, 90), 255, 0, 0);
        _strip.show();
        _strip.setPixelColor(random(0, 90), 255, 255, 255);
        _strip.show();
        _strip.setPixelColor(random(0, 90), 0, 0, 255);
        _strip.show();
    }

    delay(50);
}
