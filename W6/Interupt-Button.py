import RPi.GPIO as GPIO # type: ignore
import time

BUTTON_PIN = 17  # GPIO pin

# Set mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Callback function for interrupt
def button_callback(channel):
    print("💥 Button was pushed!")

# Set up interrupt
GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=button_callback, bouncetime=300)

print("✨ Waiting for button press (Ctrl+C to exit)...")
try:
    while True:
        time.sleep(0.1)  # Don't hog the CPU
except KeyboardInterrupt:
    print("👋 Exiting gracefully.")
finally:
    GPIO.cleanup()
