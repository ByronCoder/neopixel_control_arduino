# CircuitPython NeoPixel Setup Guide

## Step-by-Step Installation for Adafruit ESP32-S2 Qtpy

### Prerequisites

- Adafruit ESP32-S2 Qtpy board
- NeoPixel strip (WS2812B or compatible)
- USB-C cable
- 5V power supply (for NeoPixels)
- Button (optional, for pattern cycling)

### Step 1: Install CircuitPython

1. **Download CircuitPython**:
   - Go to [circuitpython.org](https://circuitpython.org/)
   - Find the ESP32-S2 Qtpy board
   - Download the latest CircuitPython firmware

2. **Flash CircuitPython**:
   - Connect your ESP32-S2 Qtpy via USB
   - Double-click the reset button to enter bootloader mode
   - Copy the downloaded `.uf2` file to the `RPI-RP2` drive
   - The board will restart and show a `CIRCUITPY` drive

### Step 2: Install Required Libraries

All required libraries are included with CircuitPython by default:
- `board` - Pin definitions
- `neopixel` - NeoPixel control
- `digitalio` - Digital I/O
- `time` - Time functions
- `random` - Random number generation
- `supervisor` - System supervision

### Step 3: Copy Project Files

1. **Create Directory Structure**:
   ```
   /CIRCUITPY/
   ├── code.py
   └── patterns/
       ├── __init__.py
       ├── base_pattern.py
       ├── fall_pattern.py
       ├── july_pattern.py
       ├── xmas_pattern.py
       ├── norm_pattern.py
       ├── alert_pattern.py
       ├── blue_pattern.py
       └── pink_pattern.py
   ```

2. **Copy Files**:
   - Copy `circuitpython_main.py` to `code.py` on the CIRCUITPY drive
   - Copy the entire `patterns/` folder to the CIRCUITPY drive

### Step 4: Hardware Connections

#### NeoPixel Strip Connection

| NeoPixel Strip | ESP32-S2 Qtpy | Description |
|----------------|----------------|-------------|
| DIN (Data In)  | D5            | Data line |
| VCC            | 5V            | Power (use external 5V supply) |
| GND            | GND           | Ground |

#### Button Connection (Optional)

| Button | ESP32-S2 Qtpy | Description |
|--------|---------------|-------------|
| One terminal | D4 | Pattern cycling input |
| Other terminal | GND | Ground |

**Note**: Use a 10kΩ pull-up resistor between D4 and 3.3V if your button doesn't have built-in pull-up.

### Step 5: Power Supply Setup

**Important**: NeoPixels require 5V power and can draw significant current.

1. **For Small Strips** (< 30 LEDs):
   - Can use USB 5V power
   - Add a large capacitor (1000µF) between 5V and GND

2. **For Large Strips** (≥ 30 LEDs):
   - Use external 5V power supply
   - Connect power supply ground to ESP32-S2 GND
   - Connect power supply 5V to NeoPixel VCC
   - Keep data line connected to ESP32-S2 D5

### Step 6: Configuration

Edit `code.py` to match your setup:

```python
# Configuration
NEOPIXEL_PIN = board.D5  # Change if using different pin
BUTTON_PIN = board.D4    # Change if using different pin
NUM_PIXELS = 90          # Set to your strip length
BRIGHTNESS = 0.3         # Adjust brightness (0.0 to 1.0)
```

### Step 7: Testing

1. **Basic Test**:
   - Copy `example_simple.py` to `code.py` for basic testing
   - Should see red, green, blue, and rainbow patterns

2. **Full System Test**:
   - Copy `circuitpython_main.py` to `code.py`
   - Should start with fall pattern
   - Press button to cycle through patterns
   - Send serial data to stop patterns

### Step 8: Serial Monitoring

Connect to the serial console to see debug messages:

**Windows**:
```bash
# Using PuTTY
# Connect to COM port at 115200 baud
```

**Mac/Linux**:
```bash
# Using screen
screen /dev/ttyACM0 115200

# Using minicom
minicom -D /dev/ttyACM0 -b 115200
```

### Troubleshooting

#### NeoPixels Not Lighting

1. **Check Power**:
   - Verify 5V power supply
   - Check current rating (60mA per LED)
   - Add capacitor if using USB power

2. **Check Connections**:
   - Verify data line connection
   - Check ground connection
   - Ensure proper pin assignment

3. **Check Code**:
   - Verify `NUM_PIXELS` matches strip length
   - Check pin assignments in code
   - Ensure CircuitPython is running

#### Button Not Working

1. **Check Wiring**:
   - Verify button connections
   - Add pull-up resistor if needed
   - Check for loose connections

2. **Check Code**:
   - Verify button pin assignment
   - Check button logic (active low)

#### Performance Issues

1. **Reduce Brightness**:
   ```python
   BRIGHTNESS = 0.1  # Lower brightness
   ```

2. **Reduce Number of Pixels**:
   ```python
   NUM_PIXELS = 30  # Test with fewer pixels
   ```

3. **Check Power Supply**:
   - Ensure adequate current capacity
   - Use external power for large strips

### Advanced Configuration

#### Custom Patterns

1. **Create New Pattern**:
   ```python
   # In patterns/my_pattern.py
   from .base_pattern import BasePattern
   
   class MyPattern(BasePattern):
       def start(self):
           while True:
               if supervisor.runtime.serial_bytes_available:
                   break
               self.color_wipe((255, 0, 0), 50)
   ```

2. **Add to Main Program**:
   ```python
   # In code.py
   from patterns.my_pattern import MyPattern
   
   patterns = [
       # ... existing patterns ...
       MyPattern(pixels, NUM_PIXELS)
   ]
   ```

#### Pin Modifications

Change pins in `code.py`:
```python
NEOPIXEL_PIN = board.D1  # Different NeoPixel pin
BUTTON_PIN = board.D2    # Different button pin
```

### Safety Notes

1. **Power Safety**:
   - Never exceed 5V for NeoPixels
   - Use adequate current capacity
   - Add fuses for large installations

2. **ESD Protection**:
   - Handle NeoPixels carefully
   - Use ESD protection when possible

3. **Heat Management**:
   - NeoPixels can get hot at full brightness
   - Ensure adequate ventilation
   - Consider heat sinks for large installations

### Support Resources

- [CircuitPython Documentation](https://docs.circuitpython.org/)
- [Adafruit NeoPixel Guide](https://learn.adafruit.com/adafruit-neopixel-uberguide)
- [ESP32-S2 Qtpy Guide](https://learn.adafruit.com/adafruit-qt-py-esp32-s2)
- [Adafruit Forums](https://forums.adafruit.com/) 