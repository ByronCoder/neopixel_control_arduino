"""
Configuration file for CircuitPython NeoPixel Control with Adafruit.IO
Copy this file to your CIRCUITPY drive and update with your credentials
"""

# WiFi Configuration
WIFI_SSID = "your_wifi_ssid_here"
WIFI_PASSWORD = "your_wifi_password_here"

# Adafruit.IO Configuration
AIO_USERNAME = "your_adafruit_io_username_here"
AIO_KEY = "your_adafruit_io_key_here"
AIO_FEED = "neopixel-pattern"  # Feed name for pattern control

# NeoPixel Configuration
NEOPIXEL_PIN = "board.D5"  # NeoPixel data pin
NUM_PIXELS = 90            # Number of pixels in your strip
BRIGHTNESS = 0.3           # Brightness (0.0 to 1.0)

# Pattern Configuration
PATTERN_NAMES = [
    "fall",
    "july", 
    "xmas",
    "normal",
    "alert",
    "blue",
    "pink"
]

# Adafruit.IO Feed Settings
# Create a feed named "neopixel-pattern" in your Adafruit.IO dashboard
# Set the feed type to "Text" or "Number"
# For text feed, use pattern names: fall, july, xmas, normal, alert, blue, pink
# For number feed, use: 0, 1, 2, 3, 4, 5, 6 