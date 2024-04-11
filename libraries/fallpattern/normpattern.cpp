#include <Arduino.h>
#include <normpattern.h>
#include <Adafruit_NeoPixel.h>

NormPattern::NormPattern(Adafruit_NeoPixel strip, int num_pixels, int pin)
{
    _strip = strip;
    _num_pixels = num_pixels;
    _pin = pin;
}

void NormPattern::start()
{
    while (true)
    {
        if (Serial.available() > 0)
        {
            break;
        }

        // Fill along the length of the strip in various colors...
        colorWipe(_strip.Color(255, 0, 0), 50); // Red
        colorWipe(_strip.Color(0, 255, 0), 50); // Green
        colorWipe(_strip.Color(0, 0, 255), 50); // Blue

        // Do a theater marquee effect in various colors...
        theaterChase(_strip.Color(127, 127, 127), 50); // White, half brightness
        theaterChase(_strip.Color(127, 0, 0), 50);     // Red, half brightness
        theaterChase(_strip.Color(0, 0, 127), 50);     // Blue, half brightness

        rainbow(10);             // Flowing rainbow cycle along the whole strip
        theaterChaseRainbow(50); // Rainbow-enhanced theaterChase variant
    }
}

void NormPattern::colorWipe(uint32_t c, uint8_t wait)
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

void NormPattern::theaterChase(uint32_t color, uint8_t wait)
{

    for (int j = 0; j < 10; j++)
    {
        if (Serial.available() > 0)
        {

            break;
        }
        for (int a = 0; a < 10; a++)
        {
            if (Serial.available() > 0)
            {

                break;
            }

            // Repeat 10 times...
            for (int b = 0; b < 3; b++)
            {

                if (Serial.available() > 0)
                {

                    break;
                }

                //  'b' counts from 0 to 2...
                _strip.clear(); //   Set all pixels in RAM to 0 (off)
                // 'c' counts up from 'b' to end of strip in steps of 3...
                for (int c = b; c < _strip.numPixels(); c += 3)
                {
                    if (Serial.available() > 0)
                    {

                        break;
                    }
                    _strip.setPixelColor(c, color); // Set pixel 'c' to value 'color'
                }
                _strip.show(); // Update strip with new contents
                delay(wait);   // Pause for a moment
            }
        }
    }
}

void NormPattern::rainbow(int wait)
{
    // Hue of first pixel runs 5 complete loops through the color wheel.
    // Color wheel has a range of 65536 but it's OK if we roll over, so
    // just count from 0 to 5*65536. Adding 256 to firstPixelHue each time
    // means we'll make 5*65536/256 = 1280 passes through this outer loop:
    for (long firstPixelHue = 0; firstPixelHue < 5 * 65536; firstPixelHue += 256)
    {
        if (Serial.available() > 0)
        {

            break;
        }
        for (int i = 0; i < _strip.numPixels(); i++)
        {
            if (Serial.available() > 0)
            {

                break;
            }
            // For each pixel in strip...
            // Offset pixel hue by an amount to make one full revolution of the
            // color wheel (range of 65536) along the length of the strip
            // (strip.numPixels() steps):
            int pixelHue = firstPixelHue + (i * 65536L / _strip.numPixels());
            // strip.ColorHSV() can take 1 or 3 arguments: a hue (0 to 65535) or
            // optionally add saturation and value (brightness) (each 0 to 255).
            // Here we're using just the single-argument hue variant. The result
            // is passed through strip.gamma32() to provide 'truer' colors
            // before assigning to each pixel:
            _strip.setPixelColor(i, _strip.gamma32(_strip.ColorHSV(pixelHue)));
        }
        _strip.show(); // Update strip with new contents
        delay(wait);   // Pause for a moment
    }
}

void NormPattern::theaterChaseRainbow(int wait)
{
    int firstPixelHue = 0; // First pixel starts at red (hue 0)
    for (int a = 0; a < 30; a++)
    {
        if (Serial.available() > 0)
        {

            break;
        }
        // Repeat 30 times...
        for (int b = 0; b < 3; b++)
        {

            if (Serial.available() > 0)
            {

                break;
            }               //  'b' counts from 0 to 2...
            _strip.clear(); //   Set all pixels in RAM to 0 (off)
            // 'c' counts up from 'b' to end of strip in increments of 3...
            for (int c = b; c < _strip.numPixels(); c += 3)
            {
                if (Serial.available() > 0)
                {

                    break;
                }

                // hue of pixel 'c' is offset by an amount to make one full
                // revolution of the color wheel (range 65536) along the length
                // of the strip (strip.numPixels() steps):
                int hue = firstPixelHue + c * 65536L / _strip.numPixels();
                uint32_t color = _strip.gamma32(_strip.ColorHSV(hue)); // hue -> RGB
                _strip.setPixelColor(c, color);                        // Set pixel 'c' to value 'color'
            }
            _strip.show();               // Update strip with new contents
            delay(wait);                 // Pause for a moment
            firstPixelHue += 65536 / 90; // One cycle of color wheel over 90 frames
        }
    }
}