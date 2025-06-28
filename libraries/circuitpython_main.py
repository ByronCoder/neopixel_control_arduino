"""
CircuitPython NeoPixel Control for Adafruit ESP32-S2 Qtpy
Translated from Arduino project with Adafruit.IO integration

This project provides various LED patterns for NeoPixel strips including:
- Fall patterns (red, yellow, orange)
- July patterns (red, white, blue) 
- Christmas patterns (red, green, white)
- Normal patterns
- Alert patterns
- Blue patterns
- Pink patterns

Hardware:
- Adafruit ESP32-S2 Qtpy
- NeoPixel strip connected to pin D5 (default)
- WiFi connectivity for Adafruit.IO control

Control:
- Adafruit.IO dashboard for pattern selection
- Serial input to break patterns
"""

import board
import neopixel
import time
import random
import wifi
import socketpool
import ssl
import adafruit_requests
import supervisor
import json
from adafruit_seesaw import seesaw, neopixel
import busio
 # Default NeoPixel pin for Qtpy

# Import configuration
try:
    from config import *
except ImportError:
    print("config.py not found. Using default configuration.")
    # Default configuration
    WIFI_SSID = "your_wifi_ssid"
    WIFI_PASSWORD = "your_wifi_password"
    AIO_USERNAME = "your_adafruit_io_username"
    AIO_KEY = "your_adafruit_io_key"
    AIO_FEED = "neopixel-pattern"
    NUM_PIXELS = 90
    BRIGHTNESS = 0.3
    PATTERN_NAMES = ["fall", "july", "xmas", "normal", "alert", "blue", "pink"]

# Configuration

i2c = busio.I2C(board.SCL1, board.SDA1)
ss = seesaw.Seesaw(i2c, addr=0x60)

NEOPIXEL_PIN = 15  # Default NeoPixel pin for Qtpy

# Initialize NeoPixels
pixels = neopixel.NeoPixel(ss, NEOPIXEL_PIN, NUM_PIXELS, brightness = 1.0, auto_write = False, pixel_order = neopixel.GRB)

# Pattern classes
from patterns.fall_pattern import FallPattern
from patterns.july_pattern import JulyPattern
from patterns.xmas_pattern import XmasPattern
from patterns.norm_pattern import NormPattern
from patterns.alert_pattern import AlertPattern
from patterns.blue_pattern import BluePattern
from patterns.pink_pattern import PinkPattern

# Pattern instances
patterns = [
    FallPattern(pixels, NUM_PIXELS),
    JulyPattern(pixels, NUM_PIXELS),
    XmasPattern(pixels, NUM_PIXELS),
    NormPattern(pixels, NUM_PIXELS),
    AlertPattern(pixels, NUM_PIXELS),
    BluePattern(pixels, NUM_PIXELS),
    PinkPattern(pixels, NUM_PIXELS)
]

current_pattern = 0
last_pattern = -1
requests = None
adafruit_io_connected = False
pattern_state = {}  # Store pattern state for smooth transitions

def connect_wifi():
    """Connect to WiFi network"""
    print(f"Connecting to WiFi: {WIFI_SSID}")
    
    try:
        wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
        print(f"Connected to WiFi: {wifi.radio.ipv4_address}")
        return True
    except Exception as e:
        print(f"WiFi connection failed: {e}")
        return False

def setup_adafruit_io():
    """Setup Adafruit.IO connection"""
    global requests, adafruit_io_connected
    
    if not connect_wifi():
        return False
        
    try:
        pool = socketpool.SocketPool(wifi.radio)
        requests = adafruit_requests.Session(pool, ssl.create_default_context())
        print("Adafruit.IO connection setup complete")
        adafruit_io_connected = True
        return True
    except Exception as e:
        print(f"Adafruit.IO setup failed: {e}")
        adafruit_io_connected = False
        return False

def get_pattern_from_adafruit_io():
    """Get current pattern selection from Adafruit.IO"""
    global requests, current_pattern, adafruit_io_connected
    
    if not requests or not adafruit_io_connected:
        return current_pattern
        
    try:
        url = f"https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{AIO_FEED}/data/last"
        headers = {"X-AIO-Key": AIO_KEY}
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            pattern_value = data.get("value", "").lower().strip()
            
            # Check for "off" command first
            if pattern_value == "off":
                return -1  # Special value for "off" state
            
            # Find pattern index by name
            for i, name in enumerate(PATTERN_NAMES):
                if pattern_value == name:
                    return i
                    
            # If numeric value is sent, use that directly
            try:
                pattern_num = int(pattern_value)
                if 0 <= pattern_num < len(patterns):
                    return pattern_num
            except ValueError:
                pass
                
        return current_pattern
        
    except Exception as e:
        print(f"Error getting pattern from Adafruit.IO: {e}")
        return current_pattern

def send_status_to_adafruit_io(pattern_name):
    """Send current pattern status to Adafruit.IO"""
    global requests, adafruit_io_connected
    
    if not requests or not adafruit_io_connected:
        return
        
    try:
        url = f"https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{AIO_FEED}/data"
        headers = {"X-AIO-Key": AIO_KEY, "Content-Type": "application/json"}
        data = {"value": pattern_name}
        
        response = requests.post(url, headers=headers, json=data)
        
        # Accept both 200 and 201 as successful responses
        if response.status_code in [200, 201]:
            print(f"Status sent to Adafruit.IO: {pattern_name} (Status: {response.status_code})")
        else:
            print(f"Failed to send status: {response.status_code}")
            
    except Exception as e:
        print(f"Error sending status to Adafruit.IO: {e}")

def initialize_adafruit_io_feed():
    """Initialize the Adafruit.IO feed with a default pattern if it's empty"""
    global requests, adafruit_io_connected
    
    if not requests or not adafruit_io_connected:
        return
        
    try:
        # Check if feed has any data
        url = f"https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{AIO_FEED}/data/last"
        headers = {"X-AIO-Key": AIO_KEY}
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            # If feed is empty or has no valid data, set default
            if not data or not data.get("value"):
                send_status_to_adafruit_io(PATTERN_NAMES[current_pattern])
                print(f"Initialized feed with default pattern: {PATTERN_NAMES[current_pattern]}")
        else:
            # If we can't read the feed, try to set a default
            send_status_to_adafruit_io(PATTERN_NAMES[current_pattern])
            print(f"Set default pattern in feed: {PATTERN_NAMES[current_pattern]}")
            
    except Exception as e:
        print(f"Error initializing Adafruit.IO feed: {e}")

def run_pattern_step(pattern_index):
    """Run one step of the current pattern"""
    global pattern_state
    
    pattern = patterns[pattern_index]
    pattern_name = PATTERN_NAMES[pattern_index]
    
    # Initialize pattern state if needed
    if pattern_name not in pattern_state:
        pattern_state[pattern_name] = {"step": 0, "last_update": 0}
    
    state = pattern_state[pattern_name]
    current_time = time.monotonic()
    
    # Run pattern-specific logic
    if pattern_name == "fall":
        return run_fall_pattern_step(pattern, state, current_time)
    elif pattern_name == "july":
        return run_july_pattern_step(pattern, state, current_time)
    elif pattern_name == "xmas":
        return run_xmas_pattern_step(pattern, state, current_time)
    elif pattern_name == "normal":
        return run_normal_pattern_step(pattern, state, current_time)
    elif pattern_name == "alert":
        return run_alert_pattern_step(pattern, state, current_time)
    elif pattern_name == "blue":
        return run_blue_pattern_step(pattern, state, current_time)
    elif pattern_name == "pink":
        return run_pink_pattern_step(pattern, state, current_time)
    
    return True  # Continue pattern

def run_fall_pattern_step(pattern, state, current_time):
    """Run one step of fall pattern"""
    if current_time - state["last_update"] < 0.05:  # 50ms delay
        return True
    
    step = state["step"] % 8  # 8 different phases
    
    if step == 0:
        pattern.color_wipe((255, 0, 0), 20)  # Red - faster
    elif step == 1:
        pattern.color_wipe((255, 255, 15), 20)  # Yellow - faster
    elif step == 2:
        pattern.color_wipe((255, 35, 0), 20)  # Orange - faster
    elif step == 3:
        pattern.theater_chase((255, 255, 15), 30)  # Yellow chase
    elif step == 4:
        pattern.theater_chase((255, 0, 0), 30)  # Red chase
    elif step == 5:
        pattern.theater_chase((255, 35, 0), 30)  # Orange chase
    elif step == 6:
        return run_fall_pattern1_step(pattern, state, current_time)
    elif step == 7:
        return run_fall_pattern2_step(pattern, state, current_time)
    
    state["step"] += 1
    state["last_update"] = current_time
    return True

def run_fall_pattern1_step(pattern, state, current_time):
    """Run one step of fall pattern 1 - alternating red, orange, yellow"""
    # Initialize sub-step if not present
    if "sub_step" not in state:
        state["sub_step"] = 0
        state["r"] = 0
        state["o"] = 1
        state["y"] = 2
    
    # Run for 100 steps (5 seconds at 50ms intervals)
    if state["sub_step"] >= 100:
        state["step"] += 1
        state["last_update"] = current_time
        state.pop("sub_step", None)
        state.pop("r", None)
        state.pop("o", None)
        state.pop("y", None)
        return True
    
    # Set red pixels
    if state["r"] < pattern.num_pixels:
        pattern.set_pixel(state["r"], (255, 0, 0))
        state["r"] += 3
        
    # Set orange pixels
    if state["o"] < pattern.num_pixels:
        pattern.set_pixel(state["o"], (255, 35, 0))
        state["o"] += 3
        
    # Set yellow pixels
    if state["y"] < pattern.num_pixels:
        pattern.set_pixel(state["y"], (255, 255, 15))
        state["y"] += 3
        
    pattern.show()
    state["sub_step"] += 1
    return True

def run_fall_pattern2_step(pattern, state, current_time):
    """Run one step of fall pattern 2 - random fall color twinkling"""
    # Initialize sub-step if not present
    if "sub_step" not in state:
        state["sub_step"] = 0
    
    # Run for 200 steps (10 seconds at 50ms intervals)
    if state["sub_step"] >= 200:
        state["step"] += 1
        state["last_update"] = current_time
        state.pop("sub_step", None)
        return True
    
    # Random red pixel
    pattern.set_pixel(random.randint(0, pattern.num_pixels - 1), (255, 0, 0))
    pattern.show()
    
    # Random yellow pixel
    pattern.set_pixel(random.randint(0, pattern.num_pixels - 1), (255, 255, 15))
    pattern.show()
    
    # Random orange pixel
    pattern.set_pixel(random.randint(0, pattern.num_pixels - 1), (255, 35, 0))
    pattern.show()
    
    state["sub_step"] += 1
    return True

def run_july_pattern_step(pattern, state, current_time):
    """Run one step of july pattern"""
    if current_time - state["last_update"] < 0.05:  # 50ms delay
        return True
    
    step = state["step"] % 8  # 8 different phases
    
    if step == 0:
        pattern.color_wipe((255, 0, 0), 20)  # Red - faster
    elif step == 1:
        pattern.color_wipe((255, 255, 255), 20)  # White - faster
    elif step == 2:
        pattern.color_wipe((0, 0, 255), 20)  # Blue - faster
    elif step == 3:
        pattern.theater_chase((255, 255, 255), 30)  # White chase
    elif step == 4:
        pattern.theater_chase((255, 0, 0), 30)  # Red chase
    elif step == 5:
        pattern.theater_chase((0, 0, 255), 30)  # Blue chase
    elif step == 6:
        return run_july_pattern1_step(pattern, state, current_time)
    elif step == 7:
        return run_july_pattern2_step(pattern, state, current_time)
    
    state["step"] += 1
    state["last_update"] = current_time
    return True

def run_july_pattern1_step(pattern, state, current_time):
    """Run one step of july pattern 1 - alternating red, blue, white"""
    # Initialize sub-step if not present
    if "sub_step" not in state:
        state["sub_step"] = 0
        state["r"] = 0
        state["b"] = 1
        state["w"] = 2
    
    # Run for 100 steps (5 seconds at 50ms intervals)
    if state["sub_step"] >= 100:
        state["step"] += 1
        state["last_update"] = current_time
        state.pop("sub_step", None)
        state.pop("r", None)
        state.pop("b", None)
        state.pop("w", None)
        return True
    
    # Set red pixels
    if state["r"] < pattern.num_pixels:
        pattern.set_pixel(state["r"], (255, 0, 0))
        state["r"] += 3
        
    # Set blue pixels
    if state["b"] < pattern.num_pixels:
        pattern.set_pixel(state["b"], (0, 0, 255))
        state["b"] += 3
        
    # Set white pixels
    if state["w"] < pattern.num_pixels:
        pattern.set_pixel(state["w"], (255, 255, 255))
        state["w"] += 3
        
    pattern.show()
    state["sub_step"] += 1
    return True

def run_july_pattern2_step(pattern, state, current_time):
    """Run one step of july pattern 2 - random patriotic color twinkling"""
    # Initialize sub-step if not present
    if "sub_step" not in state:
        state["sub_step"] = 0
    
    # Run for 200 steps (10 seconds at 50ms intervals)
    if state["sub_step"] >= 200:
        state["step"] += 1
        state["last_update"] = current_time
        state.pop("sub_step", None)
        return True
    
    # Random red pixel
    pattern.set_pixel(random.randint(0, pattern.num_pixels - 1), (255, 0, 0))
    pattern.show()
    
    # Random white pixel
    pattern.set_pixel(random.randint(0, pattern.num_pixels - 1), (255, 255, 255))
    pattern.show()
    
    # Random blue pixel
    pattern.set_pixel(random.randint(0, pattern.num_pixels - 1), (0, 0, 255))
    pattern.show()
    
    state["sub_step"] += 1
    return True

def run_xmas_pattern_step(pattern, state, current_time):
    """Run one step of xmas pattern"""
    if current_time - state["last_update"] < 0.1:  # 100ms delay
        return True
    
    step = state["step"] % 12  # 12 different phases
    
    if step == 0:
        pattern.candy_cane(5, 8, 30)  # Shorter candy cane
    elif step == 1:
        pattern.rainbow_stripe(2, 4, 50)  # Shorter rainbow
    elif step == 2:
        pattern.random_white(10, 100)  # Shorter random white
    elif step == 3:
        pattern.random_color(10, 100)  # Shorter random color
    elif step == 4:
        pattern.color_wipe((255, 0, 0), 30)  # Red
    elif step == 5:
        pattern.color_wipe((0, 255, 0), 30)  # Green
    elif step == 6:
        pattern.color_wipe((255, 255, 255), 30)  # White
    elif step == 7:
        pattern.rainbow_cycle(3, 5)  # Shorter rainbow cycle
    elif step == 8:
        pattern.alternate_color((255, 0, 0), (0, 255, 0), 50)  # Red/Green
    elif step == 9:
        pattern.random_position_fill((255, 0, 0), 30)  # Red fill
    elif step == 10:
        pattern.middle_fill((0, 255, 0), 30)  # Green middle fill
    elif step == 11:
        pattern.side_fill((255, 255, 255), 30)  # White side fill
    
    state["step"] += 1
    state["last_update"] = current_time
    return True

def run_normal_pattern_step(pattern, state, current_time):
    """Run one step of normal pattern"""
    if current_time - state["last_update"] < 0.05:  # 50ms delay
        return True
    
    step = state["step"] % 6  # 6 different phases
    
    if step == 0:
        pattern.color_wipe((255, 0, 0), 20)  # Red - faster
    elif step == 1:
        pattern.color_wipe((0, 255, 0), 20)  # Green - faster
    elif step == 2:
        pattern.color_wipe((0, 0, 255), 20)  # Blue - faster
    elif step == 3:
        pattern.theater_chase((127, 127, 127), 30)  # White chase
    elif step == 4:
        pattern.rainbow(5)  # Shorter rainbow
    elif step == 5:
        pattern.theater_chase_rainbow(30)  # Rainbow chase
    
    state["step"] += 1
    state["last_update"] = current_time
    return True

def run_alert_pattern_step(pattern, state, current_time):
    """Run one step of alert pattern"""
    if current_time - state["last_update"] < 0.05:  # 50ms delay
        return True
    
    pattern.color_wipe((255, 255, 0), 20)  # Yellow - faster
    state["last_update"] = current_time
    return True

def run_blue_pattern_step(pattern, state, current_time):
    """Run one step of blue pattern"""
    if current_time - state["last_update"] < 0.1:  # 100ms delay
        return True
    
    pattern.color_wipe((0, 0, 255), 50)  # Blue
    state["last_update"] = current_time
    return True

def run_pink_pattern_step(pattern, state, current_time):
    """Run one step of pink pattern"""
    if current_time - state["last_update"] < 0.1:  # 100ms delay
        return True
    
    pattern.color_wipe((255, 0, 255), 50)  # Pink
    state["last_update"] = current_time
    return True

def main():
    """Main loop"""
    global current_pattern, last_pattern, adafruit_io_connected
    
    print("CircuitPython NeoPixel Control Starting...")
    print(f"Number of patterns: {len(patterns)}")
    
    # Setup Adafruit.IO
    if setup_adafruit_io():
        print("Adafruit.IO connected successfully")
        # Initialize feed with current pattern
        initialize_adafruit_io_feed()
    else:
        print("Adafruit.IO setup failed - using default pattern")
    
    # Clear all pixels initially
    pixels.fill((0, 0, 0))
    pixels.show()
    
    last_check_time = 0
    check_interval = 0.5  # Check for pattern changes every 0.5 seconds
    
    while True:
        current_time = time.monotonic()
        
        # Check for pattern change from Adafruit.IO periodically
        if current_time - last_check_time >= check_interval:
            new_pattern = get_pattern_from_adafruit_io()
            
            if new_pattern != current_pattern:
                current_pattern = new_pattern
                
                if current_pattern == -1:
                    # "off" command received - clear all pixels
                    print("Turning off all pixels")
                    pixels.fill((0, 0, 0))
                    pixels.show()
                    
                    # Send status update
                    if adafruit_io_connected:
                        try:
                            send_status_to_adafruit_io("off")
                        except Exception as e:
                            print(f"Error updating status: {e}")
                else:
                    print(f"Switching to pattern {current_pattern}: {PATTERN_NAMES[current_pattern]}")
                    pixels.fill((0, 0, 0))
                    pixels.show()
                    time.sleep(0.2)  # Shorter transition delay
                    
                    # Reset pattern state for new pattern
                    pattern_state.clear()
                    
                    # Send status update (but don't wait for it to complete)
                    if adafruit_io_connected:
                        try:
                            send_status_to_adafruit_io(PATTERN_NAMES[current_pattern])
                        except Exception as e:
                            print(f"Error updating status: {e}")
            
            last_check_time = current_time
        
        # Check for serial input to break pattern
        if supervisor.runtime.serial_bytes_available:
            break
            
        # Run one step of the current pattern (only if not in "off" state)
        if current_pattern >= 0:
            try:
                run_pattern_step(current_pattern)
            except Exception as e:
                print(f"Error in pattern {current_pattern}: {e}")
                time.sleep(0.1)

if __name__ == "__main__":
    main() 