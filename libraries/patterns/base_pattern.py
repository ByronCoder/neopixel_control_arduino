"""
Base pattern class for CircuitPython NeoPixel patterns
Provides common functionality used by all pattern classes
"""

import time
import supervisor
import random

class BasePattern:
    """Base class for all NeoPixel patterns"""
    
    def __init__(self, pixels, num_pixels):
        """
        Initialize pattern
        
        Args:
            pixels: NeoPixel object
            num_pixels: Number of pixels in the strip
        """
        self.pixels = pixels
        self.num_pixels = num_pixels
        
    def color_wipe(self, color, wait):
        """
        Fill strip with a color one pixel at a time
        
        Args:
            color: RGB tuple (r, g, b)
            wait: Delay between pixels in milliseconds
        """
        for i in range(self.num_pixels):
            if supervisor.runtime.serial_bytes_available:
                break
                
            self.pixels[i] = color
            self.pixels.show()
            time.sleep(wait / 1000.0)  # Convert ms to seconds
            
    def theater_chase(self, color, wait):
        """
        Theater-style crawling lights
        
        Args:
            color: RGB tuple (r, g, b)
            wait: Delay between steps in milliseconds
        """
        for j in range(5):  # Reduced from 10 to 5 cycles for faster animation
            if supervisor.runtime.serial_bytes_available:
                break
                
            for q in range(3):
                for i in range(0, self.num_pixels, 3):
                    self.pixels[i + q] = color
                self.pixels.show()
                time.sleep(wait / 1000.0)
                
                for i in range(0, self.num_pixels, 3):
                    self.pixels[i + q] = (0, 0, 0)
                    
    def clear(self):
        """Turn off all pixels"""
        self.pixels.fill((0, 0, 0))
        self.pixels.show()
        
    def set_pixel(self, index, color):
        """
        Set a single pixel color
        
        Args:
            index: Pixel index (0 to num_pixels-1)
            color: RGB tuple (r, g, b)
        """
        if 0 <= index < self.num_pixels:
            self.pixels[index] = color
            
    def show(self):
        """Update the display"""
        self.pixels.show()
        
    def start(self):
        """
        Start the pattern - must be implemented by subclasses
        """
        raise NotImplementedError("Subclasses must implement start() method")
        
    # Additional methods for faster animations
    def fast_color_wipe(self, color, wait=10):
        """
        Fast color wipe with shorter delays
        
        Args:
            color: RGB tuple (r, g, b)
            wait: Delay between pixels in milliseconds (default 10ms)
        """
        for i in range(self.num_pixels):
            if supervisor.runtime.serial_bytes_available:
                break
                
            self.pixels[i] = color
            if i % 3 == 0:  # Show every 3rd pixel for smoother animation
                self.pixels.show()
            time.sleep(wait / 1000.0)
        self.pixels.show()  # Final show to ensure all pixels are updated
        
    def fast_theater_chase(self, color, wait=20):
        """
        Fast theater chase with shorter delays
        
        Args:
            color: RGB tuple (r, g, b)
            wait: Delay between steps in milliseconds (default 20ms)
        """
        for j in range(3):  # Reduced cycles for faster animation
            if supervisor.runtime.serial_bytes_available:
                break
                
            for q in range(3):
                for i in range(0, self.num_pixels, 3):
                    self.pixels[i + q] = color
                self.pixels.show()
                time.sleep(wait / 1000.0)
                
                for i in range(0, self.num_pixels, 3):
                    self.pixels[i + q] = (0, 0, 0)
                    
    def rainbow_cycle(self, wait=5):
        """
        Fast rainbow cycle
        
        Args:
            wait: Delay between updates in milliseconds (default 5ms)
        """
        for j in range(256):
            if supervisor.runtime.serial_bytes_available:
                break
                
            for i in range(self.num_pixels):
                if supervisor.runtime.serial_bytes_available:
                    break
                    
                rc_index = (i * 256 // self.num_pixels) + j
                self.pixels[i] = self.wheel(rc_index & 255)
                
            self.pixels.show()
            time.sleep(wait / 1000.0)
            
    def rainbow(self, wait):
        """
        Rainbow effect that cycles through the color wheel
        
        Args:
            wait: Delay between updates in milliseconds
        """
        # Hue of first pixel runs 5 complete loops through the color wheel
        for first_pixel_hue in range(0, 5 * 65536, 256):
            if supervisor.runtime.serial_bytes_available:
                break
                
            for i in range(self.num_pixels):
                if supervisor.runtime.serial_bytes_available:
                    break
                    
                # Offset pixel hue to make one full revolution of the color wheel
                # along the length of the strip
                pixel_hue = first_pixel_hue + (i * 65536 // self.num_pixels)
                color = self.hsv_to_rgb(pixel_hue, 255, 255)
                self.set_pixel(i, color)
                
            self.show()
            time.sleep(wait / 1000.0)
            
    def theater_chase_rainbow(self, wait):
        """
        Rainbow-enhanced theater chase variant
        
        Args:
            wait: Delay between updates in milliseconds
        """
        first_pixel_hue = 0  # First pixel starts at red (hue 0)
        
        for a in range(30):  # Repeat 30 times
            if supervisor.runtime.serial_bytes_available:
                break
                
            for b in range(3):  # 'b' counts from 0 to 2
                if supervisor.runtime.serial_bytes_available:
                    break
                    
                self.clear()  # Set all pixels to off
                
                # 'c' counts up from 'b' to end of strip in increments of 3
                for c in range(b, self.num_pixels, 3):
                    if supervisor.runtime.serial_bytes_available:
                        break
                        
                    # Hue of pixel 'c' is offset to make one full revolution
                    # of the color wheel along the length of the strip
                    hue = first_pixel_hue + c * 65536 // self.num_pixels
                    color = self.hsv_to_rgb(hue, 255, 255)
                    self.set_pixel(c, color)
                    
                self.show()
                time.sleep(wait / 1000.0)
                first_pixel_hue += 65536 // 90  # One cycle over 90 frames
                
    def hsv_to_rgb(self, h, s, v):
        """
        Convert HSV to RGB color
        
        Args:
            h: Hue (0-65535)
            s: Saturation (0-255)
            v: Value (0-255)
            
        Returns:
            RGB tuple (r, g, b)
        """
        # Convert hue from 16-bit to 8-bit
        h = h >> 8
        
        if s == 0:
            return (v, v, v)
            
        # Sector 0 to 5
        sector = h // 43
        f = ((h % 43) * 6) // 256
        
        p = (v * (255 - s)) // 255
        q = (v * (255 - ((s * f) // 256))) // 255
        t = (v * (255 - ((s * (255 - f)) // 256))) // 255
        
        if sector == 0:
            return (v, t, p)
        elif sector == 1:
            return (q, v, p)
        elif sector == 2:
            return (p, v, t)
        elif sector == 3:
            return (p, q, v)
        elif sector == 4:
            return (t, p, v)
        else:
            return (v, p, q)
            
    def wheel(self, pos):
        """
        Input a value 0 to 255 to get a color value.
        The colours are a transition r - g - b - back to r.
        """
        if pos < 85:
            return (pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return (255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return (0, pos * 3, 255 - pos * 3)
            
    def candy_cane(self, sets, width, wait):
        """Candy cane pattern with red and white stripes"""
        for j in range(sets * width):
            if supervisor.runtime.serial_bytes_available:
                break
                
            for i in range(self.num_pixels):
                if supervisor.runtime.serial_bytes_available:
                    break
                    
                l = self.num_pixels - i - 1
                if ((i + j) % (width * 2)) < width:
                    self.set_pixel(l, (255, 0, 0))  # Red
                else:
                    self.set_pixel(l, (255, 255, 255))  # White
                    
            self.show()
            time.sleep(wait / 1000.0)
            
    def random_white(self, sets, wait):
        """Random white/grayscale pattern"""
        for i in range(sets):
            if supervisor.runtime.serial_bytes_available:
                break
                
            for j in range(self.num_pixels):
                if supervisor.runtime.serial_bytes_available:
                    break
                    
                v = random.randint(0, 255)
                self.set_pixel(j, (v, v, v))
                
            self.show()
            time.sleep(wait / 1000.0)
            
    def rainbow_stripe(self, sets, width, wait):
        """Rainbow stripe pattern"""
        for j in range(sets * width * 6):
            if supervisor.runtime.serial_bytes_available:
                break
                
            for i in range(self.num_pixels):
                if supervisor.runtime.serial_bytes_available:
                    break
                    
                l = self.num_pixels - i - 1
                color_index = ((i + j) // width) % 6
                
                if color_index == 0:
                    self.set_pixel(l, (255, 0, 0))  # Red
                elif color_index == 1:
                    self.set_pixel(l, (255, 255, 0))  # Yellow
                elif color_index == 2:
                    self.set_pixel(l, (0, 255, 0))  # Green
                elif color_index == 3:
                    self.set_pixel(l, (0, 255, 255))  # Cyan
                elif color_index == 4:
                    self.set_pixel(l, (0, 0, 255))  # Blue
                elif color_index == 5:
                    self.set_pixel(l, (255, 0, 255))  # Magenta
                    
            self.show()
            time.sleep(wait / 1000.0)
            
    def random_color(self, sets, wait):
        """Random color pattern"""
        for i in range(sets):
            if supervisor.runtime.serial_bytes_available:
                break
                
            for j in range(self.num_pixels):
                if supervisor.runtime.serial_bytes_available:
                    break
                    
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                self.set_pixel(j, (r, g, b))
                
            self.show()
            time.sleep(wait / 1000.0)
            
    def alternate_color(self, color1, color2, wait):
        """Alternate between two colors"""
        # Set even pixels to color1, odd to color2
        for i in range(self.num_pixels):
            if supervisor.runtime.serial_bytes_available:
                break
                
            if i % 2 == 0:
                self.set_pixel(i, color1)
            else:
                self.set_pixel(i, color2)
                
        self.show()
        time.sleep(wait / 1000.0)
        
        # Swap colors
        for i in range(self.num_pixels):
            if supervisor.runtime.serial_bytes_available:
                break
                
            if i % 2 == 0:
                self.set_pixel(i, color2)
            else:
                self.set_pixel(i, color1)
                
        self.show()
        time.sleep(wait / 1000.0)
        
    def random_position_fill(self, color, wait):
        """Fill strip by lighting random positions"""
        used = [0] * self.num_pixels
        lights = 0
        
        while lights < self.num_pixels - 1:
            if supervisor.runtime.serial_bytes_available:
                break
                
            j = random.randint(0, self.num_pixels - 1)
            if used[j] != 1:
                self.set_pixel(j, color)
                used[j] = 1
                lights += 1
                self.show()
                time.sleep(wait / 1000.0)
                
    def middle_fill(self, color, wait):
        """Fill strip from middle outward"""
        # Fill from middle outward
        for i in range(self.num_pixels // 2):
            if supervisor.runtime.serial_bytes_available:
                break
                
            self.set_pixel(self.num_pixels // 2 + i, color)
            self.set_pixel(self.num_pixels // 2 - i, color)
            self.show()
            time.sleep(wait / 1000.0)
            
        # Clear from middle outward
        for i in range(self.num_pixels // 2):
            if supervisor.runtime.serial_bytes_available:
                break
                
            self.set_pixel(i, (0, 0, 0))
            self.set_pixel(self.num_pixels - i - 1, (0, 0, 0))
            self.show()
            time.sleep(wait / 1000.0)
            
    def side_fill(self, color, wait):
        """Fill strip from sides inward"""
        # Fill from sides inward
        for i in range(self.num_pixels // 2):
            if supervisor.runtime.serial_bytes_available:
                break
                
            self.set_pixel(i, color)
            self.set_pixel(self.num_pixels - i - 1, color)
            self.show()
            time.sleep(wait / 1000.0)
            
        # Clear from middle outward
        for i in range(self.num_pixels // 2):
            if supervisor.runtime.serial_bytes_available:
                break
                
            self.set_pixel(self.num_pixels // 2 + i, (0, 0, 0))
            self.set_pixel(self.num_pixels // 2 - i, (0, 0, 0))
            self.show()
            time.sleep(wait / 1000.0) 