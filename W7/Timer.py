import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Pin for LED
LED_PIN = 17

# Set up the LED pin as an output pin
GPIO.setup(LED_PIN, GPIO.OUT)

def timer_led(duration):
    print(f"LED will turn on for {duration} seconds.")
    
    # Turn LED on
    GPIO.output(LED_PIN, GPIO.HIGH)
    
    # Wait for the specified duration
    time.sleep(duration)
    
    # Turn LED off after duration
    GPIO.output(LED_PIN, GPIO.LOW)
    
    print(f"LED turned off after {duration} seconds.")

# 5 Seconds timer
timer_led(5)

GPIO.cleanup()

