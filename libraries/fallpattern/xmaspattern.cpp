#include <Arduino.h>
#include <xmaspattern.h>
#include <Adafruit_NeoPixel.h>

#define Brightness 1 //Set brightness to 1/10th
#define Full (255/Brightness)
#define Count 90 
#define Pin 6

XmasPattern::XmasPattern(Adafruit_NeoPixel strip, int num_pixels, int pin)
{
    _strip = strip;
    _num_pixels = num_pixels;
    _pin = pin;
}

uint32_t XmasPattern::Wheel(byte WheelPos) {
  
  if(WheelPos < 85) {
   return _strip.Color((WheelPos * 3)/Brightness, (255 - WheelPos * 3)/Brightness, 0);
  } else if(WheelPos < 170) {
   WheelPos -= 85;
   return _strip.Color((255 - WheelPos * 3)/Brightness, 0, (WheelPos * 3)/Brightness);
  } else {
   WheelPos -= 170;
   return _strip.Color(0,(WheelPos * 3)/Brightness, (255 - WheelPos * 3)/Brightness);
  }
}

void XmasPattern::start()
{
    while (true)
    {
        if (Serial.available() > 0)
        {
            break;
        }

        CandyCane(30,8,50);//30 sets, 8 pixels wide, 50us delay  
        RainbowStripe(5,4,75);//5 cycles, 4 pixels wide, 50 delay
        RandomWhite(50,200);//50 sets of random grayscale
        RandomColor(50,200);//50 sets of random colors
        colorWipe(_strip.Color(Full, 0, 0), 50); // Red
        colorWipe(_strip.Color(Full, Full, 0), 50); // Yellow
        colorWipe(_strip.Color(0, Full, 0), 50); // Green
        colorWipe(_strip.Color(0, Full, Full), 50); // Cyan
        colorWipe(_strip.Color(0, 0, Full), 50); // Blue
        colorWipe(_strip.Color(Full, 0, Full), 50); // Magenta
        rainbowCycle(10,2);//10 rainbow cycles
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);
        alternateColor(_strip.Color(Full, 0, 0), _strip.Color(0, Full, 0), 100);
        alternateColor(_strip.Color(0, Full, 0), _strip.Color(Full, 0, 0), 100);

        randomColorFill(10);
        randomPositionFill(_strip.Color(0, 0, Full), 50);
        randomPositionFill(_strip.Color(0, Full, 0), 50);
        randomPositionFill(_strip.Color(Full, 0, Full), 50);
        randomPositionFill(_strip.Color(Full, 0, 0), 50);
        randomPositionFill(_strip.Color(Full, Full, 0), 50);
        middleFill(_strip.Color(Full, 0,0), 50);
        middleFill(_strip.Color(Full, Full,0), 50);
        middleFill(_strip.Color(Full, Full,Full), 50);
        middleFill(_strip.Color(0, Full,0), 50);
        middleFill(_strip.Color(Full, 0, Full), 50);
        middleFill(_strip.Color(0, Full,Full), 50);
        sideFill(_strip.Color(Full, 0,0), 50);
        sideFill(_strip.Color(Full, Full,0), 50);
        sideFill(_strip.Color(Full, 0,0), 50);
        sideFill(_strip.Color(Full, Full,0), 50);
        sideFill(_strip.Color(Full, Full,Full), 50);
        sideFill(_strip.Color(0, Full,0), 50);
        sideFill(_strip.Color(Full, 0, Full), 50);
        sideFill(_strip.Color(0, Full,Full), 50);
        
        colorWipe(0,5);//Black
          
      
    }
}

void XmasPattern::CandyCane(int sets, int width, int wait) {

 
        
  int L;
  for(int j=0;j<(sets*width);j++) {
       if (Serial.available() > 0)
        {
            break;
        }
    for(int i=0;i< _strip.numPixels();i++) {
         if (Serial.available() > 0)
        {
            break;
        }// f
      L=_strip.numPixels()-i-1;
      if ( ((i+j) % (width*2) )<width)
        _strip.setPixelColor(L,Full,0,0);
      else
        _strip.setPixelColor(L,Full,Full, Full);
    };
    _strip.show();
    delay(wait);
}
}

 void XmasPattern::RandomWhite (int sets, int wait) {
   

    int V,i,j;
  for (i=0;i<sets;i++) {
      if (Serial.available() > 0)
        {
            break;
        }
    for(j=0;j<_strip.numPixels();j++) {
         if (Serial.available() > 0)
        {
            break;
        }// f
      V=random(Full);
      _strip.setPixelColor(j,V,V,V);
    }
    _strip.show();
    delay(wait);
  }
 }

 void XmasPattern::RainbowStripe (int sets,int width,int wait) {
  

  int L;
  for(int j=0;j<(sets*width*6);j++) {
       if (Serial.available() > 0)
        {
            break;
        }
    for(int i=0;i< _strip.numPixels();i++) {
         if (Serial.available() > 0)
        {
            break;
        }// f
      L=_strip.numPixels()-i-1;
      switch ( ( (i+j)/width) % 6 ) {
        case 0: _strip.setPixelColor(L,Full,0,0);break;//Red
        case 1: _strip.setPixelColor(L,Full,Full,0);break;//Yellow
        case 2: _strip.setPixelColor(L,0,Full,0);break;//Green
        case 3: _strip.setPixelColor(L,0,Full,Full);break;//Cyan
        case 4: _strip.setPixelColor(L,0,0,Full);break;//Blue
        case 5: _strip.setPixelColor(L,Full,0,Full);break;//Magenta
//        default: strip.setPixelColor(L,0,0,0);//Use for debugging only
      }
    };
    _strip.show();
    delay(wait);
  };
};

void XmasPattern::colorWipe(uint32_t c, uint8_t wait) {
  
  for(uint16_t i=0; i< _strip.numPixels(); i++) {
      if (Serial.available() > 0)
        {
            break;
        }
      _strip.setPixelColor(i, c);
      
      _strip.show();
      delay(wait);
  }
}

void XmasPattern::RandomColor(int sets, int wait) {


  int i,j;
  for (i=0;i<sets;i++) {
        if (Serial.available() > 0)
        {
            break;
        }
    for(j=0;j<_strip.numPixels();j++) {
         if (Serial.available() > 0)
        {
            break;
        }// f
      _strip.setPixelColor(j,random(255)/Brightness,random(255)/Brightness,random(255)/Brightness);
    }
    _strip.show();
    delay(wait);
  }
};

void XmasPattern::rainbowCycle(uint8_t sets, uint8_t wait) {

  uint16_t i, j;
  for(j=0; j<256*sets; j++) { //cycles of all colors on wheel
      if (Serial.available() > 0)
        {
            break;
        }
    for(i=0; i< _strip.numPixels(); i++) {
         if (Serial.available() > 0)
        {
            break;
        }// f
      _strip.setPixelColor(_strip.numPixels()-i-1, Wheel(((i * 256 / _strip.numPixels()) + j) & 255));
    }
    _strip.show();
    delay(wait);
  }
}

void XmasPattern::alternateColor(uint32_t c1, uint32_t c2, uint8_t wait) {
   
  for(uint16_t i=0; i<_strip.numPixels(); i++) {
     if (Serial.available() > 0)
        {
            break;
        }
    if(i%2 == 0) { // set even LED to color 1
      _strip.setPixelColor(i, c1);
    } else { // set odd LED to color 2
      _strip.setPixelColor(i, c2);
    }
  }

  _strip.show(); // apply the colors
  delay(wait);

  for(uint16_t i=0; i<_strip.numPixels(); i++) {
      if (Serial.available() > 0)
        {
            break;
        }

    if(i%2 == 0) { // set even LED to color 2
      _strip.setPixelColor(i, c2);
    } else { // set odd LED to color 1
      _strip.setPixelColor(i, c1);
    }
  }

  _strip.show(); // apply the colors
  delay(wait);

  
}


// gradually fill up the strip with random colors
void XmasPattern::randomColorFill(uint8_t wait) {
  //clearStrip();
  

  for(uint16_t i=0; i<_strip.numPixels(); i++) { // iterate over every LED of the _strip
    if (Serial.available() > 0)
        {
            break;
        }
    int r = random(0,255); // generate a random color
    int g = random(0,255);
    int b = random(0,255);

    for(uint16_t j=0; j<_strip.numPixels()-i; j++) {
         if (Serial.available() > 0)
        {
            break;
        }// f // iterate over every LED of the _strip, that hasn't lit up yet
      _strip.setPixelColor(j-1, _strip.Color(0, 0, 0)); // turn previous LED off
      _strip.setPixelColor(j, _strip.Color(r, g, b)); // turn current LED on
      _strip.show(); // apply the colors
      delay(wait);
    }
  }
}

// pick a random LED to light up until entire _strip is lit
void XmasPattern::randomPositionFill(uint32_t c, uint8_t wait) {
  //clear_strip();

  
  int used[_strip.numPixels()]; // array to keep track of lit LEDs
  int lights = 0; // counter

  for(int i = 0; i<_strip.numPixels(); i++){ // fill array with 0
    if (Serial.available() > 0)
        {
            break;
        }

    used[i] = 0;
  }

  while(lights<_strip.numPixels()-1) {
       if (Serial.available() > 0)
        {
            break;
        }// f
    int j = random(0,_strip.numPixels()-1); // pick a random LED
    if(used[j] != 1){ // if LED not already lit, proceed
      _strip.setPixelColor(j, c);
      used[j] = 1; // update array to remember it is lit
      lights++;
      _strip.show(); // display
      delay(wait);
    }
  }
}

// Light up the _strip starting from the middle
void XmasPattern::middleFill(uint32_t c, uint8_t wait) {
 // clear_strip();


  for(uint16_t i=0; i<(_strip.numPixels()/2); i++) {
    
   if (Serial.available() > 0)
        {
            break;
        } // start from the middle, lighting an LED on each side
    _strip.setPixelColor(_strip.numPixels()/2 + i, c);
    _strip.setPixelColor(_strip.numPixels()/2 - i, c);
    _strip.show();
    delay(wait);
  }

  for(uint16_t i=0; i<(_strip.numPixels()/2); i++) { 
       if (Serial.available() > 0)
        {
            break;
        }// f// reverse
    _strip.setPixelColor(i, _strip.Color(0, 0, 0));
    _strip.setPixelColor(_strip.numPixels() - i, _strip.Color(0, 0, 0));
    _strip.show();
    delay(wait);
  }
}

// Light up the strip starting from the sides
void XmasPattern::sideFill(uint32_t c, uint8_t wait) {
  //clearStrip();

   

  for(uint16_t i=0; i<(_strip.numPixels()/2); i++) { 
     if (Serial.available() > 0)
        {
            break;
        }// fill _strip from sides to middle
    _strip.setPixelColor(i, c);
    _strip.setPixelColor(_strip.numPixels() - i, c);
    _strip.show();
    delay(wait);
  }

  for(uint16_t i=0; i<(_strip.numPixels()/2); i++) { 
       if (Serial.available() > 0)
        {
            break;
        }// f// reverse
    _strip.setPixelColor(_strip.numPixels()/2 + i, _strip.Color(0, 0, 0));
    _strip.setPixelColor(_strip.numPixels()/2 - i, _strip.Color(0, 0, 0));
    _strip.show();
    delay(wait);
  }
}
