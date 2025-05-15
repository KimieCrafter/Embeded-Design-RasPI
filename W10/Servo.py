import RPi.GPIO as GPIO
import time

# GPIO pins for the two servos
SERVO1_PIN = 17
SERVO2_PIN = 18

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO1_PIN, GPIO.OUT)
GPIO.setup(SERVO2_PIN, GPIO.OUT)

# Create PWM objects at 50Hz
pwm1 = GPIO.PWM(SERVO1_PIN, 50)
pwm2 = GPIO.PWM(SERVO2_PIN, 50)

pwm1.start(0)
pwm2.start(0)

def set_angle(pwm, angle):
    # Convert angle (0-180) to duty cycle
    duty = 2 + angle / 18
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.4)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        # Sweep from 0 to 180
        for angle in range(0, 181, 30):
            print("Servo1:", angle, "deg; Servo2:", 180 - angle, "deg")
            set_angle(pwm1, angle)
            set_angle(pwm2, 180 - angle)
            time.sleep(0.5)

        # Sweep back from 180 to 0
        for angle in range(180, -1, -30):
            print("Servo1:", angle, "deg; Servo2:", 180 - angle, "deg")
            set_angle(pwm1, angle)
            set_angle(pwm2, 180 - angle)
            time.sleep(0.5)

except KeyboardInterrupt:
    # Clean up on Ctrl+C
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()
    print("Clean exit")

