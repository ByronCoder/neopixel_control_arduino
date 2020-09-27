# Neopixel Control Arduino Code

### This is the Arudino code for my Neopixel control project. It uses the Arudino Serial library and the Adafruit Neopixel library. The Arduino is currently connected to a Raspberry PI via USB which runs a NodeJS server that uses Express to receive HTTP requests. When it receives a specific request the NodeJS API uses the NodeJS SerialPort library to send a specific character to an Arduino. Based on the character the Arudino starts a specific pattern.
