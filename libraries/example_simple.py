"""
Simple NeoPixel Example for Adafruit ESP32-S2 Qtpy
Basic demonstration of NeoPixel control

This example shows basic color patterns without the complex pattern system.
Useful for testing your hardware setup.
"""

import board
import neopixel
import time

# Configuration
NEOPIXEL_PIN = board.D5  # NeoPixel data pin
NUM_PIXELS = 16          # Number of pixels (adjust for your strip)
BRIGHTNESS = 0.3         # Brightness (0.0 to 1.0)

# Initialize NeoPixels
pixels = neopixel.NeoPixel(NEOPIXEL_PIN, NUM_PIXELS, brightness=BRIGHTNESS, auto_write=False)

def color_wipe(color, wait):
    """Fill strip with a color one pixel at a time"""
    for i in range(NUM_PIXELS):
        pixels[i] = color
        pixels.show()
        time.sleep(wait)

def theater_chase(color, wait):
    """Theater-style crawling lights"""
    for j in range(10):  # 10 cycles
        for q in range(3):
            for i in range(0, NUM_PIXELS, 3):
                pixels[i + q] = color
            pixels.show()
            time.sleep(wait)
            
            for i in range(0, NUM_PIXELS, 3):
                pixels[i + q] = (0, 0, 0)

def rainbow_cycle(wait):
    """Rainbow cycle along the strip"""
    for j in range(256):
        for i in range(NUM_PIXELS):
            # Calculate color based on position and time
            rc_index = (i * 256 // NUM_PIXELS) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

def wheel(pos):
    """Input a value 0 to 255 to get a color value"""
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

def main():
    """Main demonstration loop"""
    print("Starting NeoPixel demonstration...")
    
    # Clear all pixels
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(1)
    
    while True:
        print("Red wipe")
        color_wipe((255, 0, 0), 0.1)  # Red
        
        print("Green wipe") 
        color_wipe((0, 255, 0), 0.1)  # Green
        
        print("Blue wipe")
        color_wipe((0, 0, 255), 0.1)  # Blue
        
        print("White theater chase")
        theater_chase((127, 127, 127), 0.1)  # White
        
        print("Rainbow cycle")
        rainbow_cycle(0.01)  # Rainbow

if __name__ == "__main__":
    main() 