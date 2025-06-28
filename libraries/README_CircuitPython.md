# CircuitPython NeoPixel Control for Adafruit ESP32-S2 Qtpy

This project provides various LED patterns for NeoPixel strips with Adafruit.IO remote control. It's a CircuitPython translation of an Arduino NeoPixel control project.

## Features

- **7 Different Pattern Themes**: Fall, July, Christmas, Normal, Alert, Blue, and Pink
- **Adafruit.IO Remote Control**: Change patterns remotely via web dashboard
- **Fast & Smooth Animations**: Optimized for responsive visual effects
- **WiFi Connectivity**: Built-in WiFi support for remote control
- **Real-time Status Updates**: Current pattern status sent back to Adafruit.IO

## Pattern Themes

1. **Fall** - Autumn colors (red, yellow, orange) with leaf-like patterns
2. **July** - Patriotic colors (red, white, blue) for Independence Day
3. **Christmas** - Holiday colors (red, green, white) with festive effects
4. **Normal** - Standard rainbow and theater chase patterns
5. **Alert** - Warning yellow color for attention
6. **Blue** - Blue color theme
7. **Pink** - Pink color theme
8. **Off** - Turns off all pixels (send "off" via Adafruit.IO)

## Hardware Requirements

- Adafruit ESP32-S2 Qtpy
- NeoPixel strip (up to 90 pixels by default)
- WiFi connection for Adafruit.IO control

## Pin Connections

| Component | ESP32-S2 Qtpy Pin | Description |
|-----------|-------------------|-------------|
| NeoPixels | D5 | Data line (configurable) |
| NeoPixels VCC | 5V | Power supply |
| NeoPixels GND | GND | Ground |

## Setup

1. **Install CircuitPython** on your ESP32-S2 Qtpy
2. **Copy files** to the device:
   - `circuitpython_main.py` → `code.py` (main program)
   - `config.py` (configuration file)
   - `patterns/` folder (pattern classes)
   - `requirements.txt` (dependencies)
3. **Install dependencies** from `requirements.txt`
4. **Configure WiFi and Adafruit.IO** in `config.py`
5. **Connect NeoPixels** to the appropriate pin (default: D5)

## Configuration

Edit `config.py` with your settings:

```python
WIFI_SSID = "your_wifi_ssid"
WIFI_PASSWORD = "your_wifi_password"
AIO_USERNAME = "your_adafruit_io_username"
AIO_KEY = "your_adafruit_io_key"
AIO_FEED = "neopixel-pattern"
NUM_PIXELS = 90
BRIGHTNESS = 0.3
```

## Adafruit.IO Setup

1. **Create an Adafruit.IO account** at [io.adafruit.com](https://io.adafruit.com)
2. **Create a new feed** called `neopixel-pattern`
3. **Set up a dashboard** with a text block or toggle buttons
4. **Send pattern names** to the feed:
   - `fall`, `july`, `xmas`, `normal`, `alert`, `blue`, `pink`
   - `off` (turns off all pixels)

## Usage

1. **Power on** the device - it will connect to WiFi and Adafruit.IO
2. **Send pattern names** via Adafruit.IO dashboard
3. **Monitor status** - current pattern is sent back to Adafruit.IO
4. **Use "off" command** to turn off all pixels

## Pattern Details

### Fall Pattern
- Color wipes: Red, Yellow, Orange
- Theater chases with fall colors
- Alternating red/orange/yellow pattern
- Random fall color twinkling

### July Pattern
- Color wipes: Red, White, Blue
- Theater chases with patriotic colors
- Alternating red/blue/white pattern
- Random patriotic color twinkling

### Christmas Pattern
- Candy cane stripes
- Rainbow effects
- Random white and color patterns
- Red/green/white color sequences

### Normal Pattern
- Standard color wipes (red, green, blue)
- Theater chase effects
- Rainbow cycles
- Rainbow theater chase

### Alert Pattern
- Yellow warning color
- Continuous yellow color wipe

### Blue/Pink Patterns
- Single color themes
- Continuous color wipes

## Troubleshooting

- **WiFi Connection Issues**: Check SSID and password in `config.py`
- **Adafruit.IO Errors**: Verify username, key, and feed name
- **Pattern Not Changing**: Check feed name and pattern spelling
- **Pixels Not Lighting**: Verify NeoPixel connection and pin configuration

## File Structure

```
libraries/
├── circuitpython_main.py    # Main program (rename to code.py)
├── config.py                # Configuration file
├── requirements.txt         # Dependencies
├── patterns/                # Pattern classes
│   ├── __init__.py
│   ├── base_pattern.py      # Base pattern class
│   ├── fall_pattern.py      # Fall theme patterns
│   ├── july_pattern.py      # July theme patterns
│   ├── xmas_pattern.py      # Christmas theme patterns
│   ├── norm_pattern.py      # Normal patterns
│   ├── alert_pattern.py     # Alert patterns
│   ├── blue_pattern.py      # Blue theme patterns
│   └── pink_pattern.py      # Pink theme patterns
└── README_CircuitPython.md  # This file
```

## Dependencies

- `board` - Hardware interface
- `neopixel` - NeoPixel control
- `wifi` - WiFi connectivity
- `socketpool` - Network sockets
- `ssl` - Secure connections
- `adafruit_requests` - HTTP requests
- `supervisor` - Runtime control
- `time` - Timing functions
- `random` - Random number generation
- `adafruit_seesaw` - Seesaw board support
- `busio` - I2C bus interface

## License

This project is based on the Adafruit NeoPixel library and follows the same licensing terms.

## Credits

- Original Arduino code by Adafruit Industries
- CircuitPython translation for ESP32-S2 Qtpy
- Adafruit.IO integration for remote control
- Pattern implementations based on Adafruit NeoPixel examples

## Support

For issues and questions:
- Check the [CircuitPython documentation](https://docs.circuitpython.org/)
- Visit the [Adafruit forums](https://forums.adafruit.com/)
- Review the [ESP32-S2 Qtpy guide](https://learn.adafruit.com/adafruit-qt-py-esp32-s2)
- See [Adafruit.IO documentation](https://io.adafruit.com/api/docs/) 