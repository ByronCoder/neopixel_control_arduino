# Adafruit.IO Setup Guide for NeoPixel Control

This guide will help you set up Adafruit.IO to control your NeoPixel patterns remotely through a web dashboard.

## Prerequisites

- Adafruit.IO account (free at [io.adafruit.com](https://io.adafruit.com))
- ESP32-S2 Qtpy with CircuitPython
- WiFi network access
- NeoPixel strip

## Step 1: Create Adafruit.IO Account

1. Go to [io.adafruit.com](https://io.adafruit.com)
2. Sign up for a free account
3. Note your username (found in your profile)

## Step 2: Get Your Adafruit.IO Key

1. Log into your Adafruit.IO account
2. Click on your username in the top right
3. Select "My Key"
4. Copy your AIO Key (you'll need this for the config)

## Step 3: Create a Feed

1. In your Adafruit.IO dashboard, click "Feeds"
2. Click "Create a New Feed"
3. Name it `neopixel-pattern`
4. Set the feed type to "Text" (recommended) or "Number"
5. Click "Create Feed"

## Step 4: Create a Dashboard

1. Click "Dashboards" in the left sidebar
2. Click "Create a New Dashboard"
3. Name it "NeoPixel Control"
4. Click "Create Dashboard"

## Step 5: Add Controls to Dashboard

### Option A: Text Input (Recommended)

1. In your dashboard, click the "+" button
2. Select "Text Input"
3. Choose the `neopixel-pattern` feed
4. Set the input type to "Text"
5. Add these values (one per line):
   ```
   fall
   july
   xmas
   normal
   alert
   blue
   pink
   ```
6. Click "Create Block"

### Option B: Toggle Buttons

1. In your dashboard, click the "+" button
2. Select "Toggle"
3. Choose the `neopixel-pattern` feed
4. Set the ON text to a pattern name (e.g., "fall")
5. Set the OFF text to another pattern (e.g., "july")
6. Click "Create Block"
7. Repeat for other patterns

### Option C: Number Input

1. In your dashboard, click the "+" button
2. Select "Number Input"
3. Choose the `neopixel-pattern` feed
4. Set min to 0, max to 6
5. Click "Create Block"

## Step 6: Configure Your ESP32-S2

1. **Install Required Libraries**:
   - Download the CircuitPython library bundle from [circuitpython.org/libraries](https://circuitpython.org/libraries)
   - Copy the `adafruit_requests` folder to `/lib/` on your CIRCUITPY drive

2. **Update Configuration**:
   - Copy `config.py` to your CIRCUITPY drive
   - Edit `config.py` with your credentials:

```python
# WiFi Configuration
WIFI_SSID = "your_actual_wifi_ssid"
WIFI_PASSWORD = "your_actual_wifi_password"

# Adafruit.IO Configuration
AIO_USERNAME = "your_adafruit_io_username"
AIO_KEY = "your_adafruit_io_key"
AIO_FEED = "neopixel-pattern"

# NeoPixel Configuration
NUM_PIXELS = 90  # Adjust to your strip length
BRIGHTNESS = 0.3  # Adjust brightness (0.0 to 1.0)
```

3. **File Structure**:
   ```
   /CIRCUITPY/
   ├── code.py                    # Main program
   ├── config.py                  # Your configuration
   ├── test_adafruit_io.py        # Test script (optional)
   ├── lib/
   │   └── adafruit_requests/     # HTTP library
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

## Step 7: Test Your Setup

### Option A: Use the Test Script (Recommended)

1. **Rename the test script**:
   - Rename `test_adafruit_io.py` to `code.py` temporarily
   - This will run the test instead of the main program

2. **Run the test**:
   - Power on your ESP32-S2
   - Check the serial output for test results
   - The test will verify WiFi, Adafruit.IO connection, and pattern posting

3. **Expected test output**:
   ```
   Adafruit.IO Connectivity Test
   ========================================
   Testing WiFi connection to: your_wifi_ssid
   ✅ WiFi connected successfully!
      IP Address: 192.168.1.100
   
   Testing Adafruit.IO connection...
   Username: your_username
   Feed: neopixel-pattern
   Testing GET request to: https://io.adafruit.com/api/v2/...
   GET Response Status: 200
   ✅ GET request successful!
      Current feed value: None
      Last updated: Unknown
   
   Testing POST request...
   POST Response Status: 200
   ✅ POST request successful!
      Status code: 200
      Note: Status 200 is normal for some Adafruit.IO operations
   
   Testing pattern values...
   Testing pattern: fall
      ✅ fall - Status: 200
   Testing pattern: july
      ✅ july - Status: 200
   ...
   
   🎉 All tests passed! Your Adafruit.IO setup is working correctly.
   ```

### Option B: Test with Main Program

1. **Rename back to main program**:
   - Rename `code.py` back to `test_adafruit_io.py`
   - Rename `circuitpython_main.py` to `code.py`

2. **Run the main program**:
   - Power on your ESP32-S2
   - Check serial output for connection status

3. **Expected main program output**:
   ```
   CircuitPython NeoPixel Control Starting...
   Number of patterns: 7
   Connecting to WiFi: your_wifi_ssid
   Connected to WiFi: 192.168.1.100
   Adafruit.IO connection setup complete
   Adafruit.IO connected successfully
   Initialized feed with default pattern: fall
   ```

## Step 8: Control Patterns

1. **Go to your Adafruit.IO dashboard**
2. **Use the controls** to change patterns
3. **Watch your NeoPixels** change patterns
4. **Check the serial output** for status updates

## Pattern Control Methods

### Text Input Method
Send these exact text values to change patterns:
- `fall` - Autumn colors (red, yellow, orange)
- `july` - Patriotic colors (red, white, blue)
- `xmas` - Holiday colors (red, green, white, rainbow)
- `normal` - Standard patterns (rainbow, theater chase)
- `alert` - Warning pattern (yellow)
- `blue` - Blue theme
- `pink` - Pink theme

### Number Input Method
Send these numbers to change patterns:
- `0` - Fall pattern
- `1` - July pattern
- `2` - Christmas pattern
- `3` - Normal pattern
- `4` - Alert pattern
- `5` - Blue pattern
- `6` - Pink pattern

## Troubleshooting

### Status Code 200 vs 201 Issue

**Problem**: You're getting status code 200 instead of 201 when posting to Adafruit.IO.

**Solution**: This is actually normal! The updated code now accepts both 200 and 201 as successful responses. Here's why:

- **Status 201**: Standard HTTP "Created" response for successful POST requests
- **Status 200**: "OK" response, also acceptable for successful operations
- **Both are valid**: Adafruit.IO may return either depending on the operation

**Updated Code**: The main program now handles both status codes correctly:
```python
if response.status_code in [200, 201]:
    print(f"Status sent to Adafruit.IO: {pattern_name} (Status: {response.status_code})")
```

### WiFi Connection Issues

1. **Check Credentials**:
   - Verify WiFi SSID and password in `config.py`
   - Ensure WiFi network is 2.4GHz (ESP32-S2 doesn't support 5GHz)

2. **Check Signal Strength**:
   - Move ESP32-S2 closer to WiFi router
   - Check for interference from other devices

3. **Serial Output**:
   ```
   WiFi connection failed: [Errno 2] ENODEV
   ```
   This usually means incorrect WiFi credentials.

### Adafruit.IO Connection Issues

1. **Check API Key**:
   - Verify your AIO_KEY in `config.py`
   - Ensure the key is copied correctly (no extra spaces)

2. **Check Feed Name**:
   - Verify `AIO_FEED` matches exactly: `neopixel-pattern`
   - Check feed name in Adafruit.IO dashboard

3. **Check Username**:
   - Verify `AIO_USERNAME` matches your Adafruit.IO username
   - Username is case-sensitive

### Pattern Not Changing

1. **Check Feed Type**:
   - Ensure feed is set to "Text" or "Number"
   - Text feed: send pattern names exactly as listed
   - Number feed: send numbers 0-6

2. **Check Serial Output**:
   ```
   Error getting pattern from Adafruit.IO: [Errno 1] ENODEV
   ```
   This indicates network or API issues.

3. **Test with Serial Monitor**:
   - Connect to serial console to see debug messages
   - Look for pattern change confirmations

### Code Stops Running

1. **Check for Exceptions**:
   - The updated code has better error handling
   - Exceptions won't stop the main loop
   - Check serial output for error messages

2. **Test with Test Script**:
   - Use `test_adafruit_io.py` to isolate issues
   - This will help identify if the problem is WiFi, Adafruit.IO, or the main program

3. **Check Memory**:
   - ESP32-S2 has limited memory
   - Reduce `NUM_PIXELS` if using many LEDs
   - Lower `BRIGHTNESS` to reduce memory usage

### Performance Issues

1. **Reduce Update Frequency**:
   - The code checks Adafruit.IO every pattern cycle
   - For faster response, modify the check frequency

2. **Network Latency**:
   - Pattern changes may have 1-2 second delay
   - This is normal for cloud-based control

3. **Memory Management**:
   - The updated code has better memory management
   - Status updates are non-blocking

## Advanced Configuration

### Custom Pattern Names

Edit `PATTERN_NAMES` in `config.py`:
```python
PATTERN_NAMES = [
    "autumn",    # instead of "fall"
    "patriotic", # instead of "july"
    "holiday",   # instead of "xmas"
    "rainbow",   # instead of "normal"
    "warning",   # instead of "alert"
    "ocean",     # instead of "blue"
    "rose"       # instead of "pink"
]
```

### Multiple Feeds

You can control multiple aspects with different feeds:
```python
# In config.py
AIO_FEED_PATTERN = "neopixel-pattern"
AIO_FEED_BRIGHTNESS = "neopixel-brightness"
AIO_FEED_SPEED = "neopixel-speed"
```

### Security Considerations

1. **Keep Credentials Secure**:
   - Don't share your `config.py` file
   - Use environment variables if possible
   - Regularly rotate your Adafruit.IO key

2. **Network Security**:
   - Use WPA2 or WPA3 WiFi security
   - Consider using a dedicated IoT network

## Support Resources

- [Adafruit.IO Documentation](https://io.adafruit.com/api/docs/)
- [CircuitPython WiFi Guide](https://learn.adafruit.com/pico-w-wifi-with-circuitpython)
- [Adafruit.IO Forum](https://forums.adafruit.com/viewforum.php?f=56)
- [ESP32-S2 Qtpy Guide](https://learn.adafruit.com/adafruit-qt-py-esp32-s2)

## Example Dashboard Layout

Here's a suggested dashboard layout:

```
┌─────────────────────────────────────┐
│           NeoPixel Control          │
├─────────────────────────────────────┤
│ Pattern: [Text Input] [Send]        │
├─────────────────────────────────────┤
│ [Fall] [July] [Xmas] [Normal]       │
│ [Alert] [Blue] [Pink]               │
├─────────────────────────────────────┤
│ Current Pattern: fall               │
│ Last Updated: 2024-01-15 14:30:25  │
└─────────────────────────────────────┘
``` 