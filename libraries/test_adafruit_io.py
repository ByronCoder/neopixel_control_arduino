"""
Test script for Adafruit.IO connectivity
Use this to test your Adafruit.IO setup before running the main program
"""

import wifi
import socketpool
import ssl
import adafruit_requests
import time

# Import configuration
try:
    from config import *
except ImportError:
    print("config.py not found. Using default configuration.")
    WIFI_SSID = "your_wifi_ssid"
    WIFI_PASSWORD = "your_wifi_password"
    AIO_USERNAME = "your_adafruit_io_username"
    AIO_KEY = "your_adafruit_io_key"
    AIO_FEED = "neopixel-pattern"

def test_wifi():
    """Test WiFi connection"""
    print(f"Testing WiFi connection to: {WIFI_SSID}")
    
    try:
        wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
        print(f"✅ WiFi connected successfully!")
        print(f"   IP Address: {wifi.radio.ipv4_address}")
        return True
    except Exception as e:
        print(f"❌ WiFi connection failed: {e}")
        return False

def test_adafruit_io_connection():
    """Test Adafruit.IO connection"""
    print(f"\nTesting Adafruit.IO connection...")
    print(f"Username: {AIO_USERNAME}")
    print(f"Feed: {AIO_FEED}")
    
    try:
        pool = socketpool.SocketPool(wifi.radio)
        requests = adafruit_requests.Session(pool, ssl.create_default_context())
        
        # Test GET request
        url = f"https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{AIO_FEED}/data/last"
        headers = {"X-AIO-Key": AIO_KEY}
        
        print(f"Testing GET request to: {url}")
        response = requests.get(url, headers=headers)
        
        print(f"GET Response Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ GET request successful!")
            print(f"   Current feed value: {data.get('value', 'None')}")
            print(f"   Last updated: {data.get('created_at', 'Unknown')}")
        else:
            print(f"❌ GET request failed with status: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
        
        # Test POST request
        print(f"\nTesting POST request...")
        post_url = f"https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{AIO_FEED}/data"
        post_headers = {"X-AIO-Key": AIO_KEY, "Content-Type": "application/json"}
        post_data = {"value": "test"}
        
        response = requests.post(post_url, headers=post_headers, json=post_data)
        
        print(f"POST Response Status: {response.status_code}")
        
        if response.status_code in [200, 201]:
            print(f"✅ POST request successful!")
            print(f"   Status code: {response.status_code}")
            if response.status_code == 200:
                print("   Note: Status 200 is normal for some Adafruit.IO operations")
            else:
                print("   Note: Status 201 is the standard success code for POST")
        else:
            print(f"❌ POST request failed with status: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Adafruit.IO connection failed: {e}")
        return False

def test_pattern_values():
    """Test sending different pattern values"""
    print(f"\nTesting pattern values...")
    
    try:
        pool = socketpool.SocketPool(wifi.radio)
        requests = adafruit_requests.Session(pool, ssl.create_default_context())
        
        pattern_names = ["fall", "july", "xmas", "normal", "alert", "blue", "pink"]
        
        for pattern in pattern_names:
            print(f"Testing pattern: {pattern}")
            
            url = f"https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{AIO_FEED}/data"
            headers = {"X-AIO-Key": AIO_KEY, "Content-Type": "application/json"}
            data = {"value": pattern}
            
            response = requests.post(url, headers=headers, json=data)
            
            if response.status_code in [200, 201]:
                print(f"   ✅ {pattern} - Status: {response.status_code}")
            else:
                print(f"   ❌ {pattern} - Status: {response.status_code}")
            
            time.sleep(1)  # Wait between requests
        
        return True
        
    except Exception as e:
        print(f"❌ Pattern testing failed: {e}")
        return False

def main():
    """Main test function"""
    print("Adafruit.IO Connectivity Test")
    print("=" * 40)
    
    # Test WiFi
    if not test_wifi():
        print("\n❌ WiFi test failed. Cannot proceed with Adafruit.IO tests.")
        return
    
    # Test Adafruit.IO connection
    if not test_adafruit_io_connection():
        print("\n❌ Adafruit.IO connection test failed.")
        return
    
    # Test pattern values
    if not test_pattern_values():
        print("\n❌ Pattern value testing failed.")
        return
    
    print("\n🎉 All tests passed! Your Adafruit.IO setup is working correctly.")
    print("\nYou can now run the main program (code.py)")

if __name__ == "__main__":
    main() 