import RPi.GPIO as GPIO
import time

def blinkLED(pin, delay):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(delay)

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(11, GPIO.OUT)

    while True:
        for i in range(5):
            blinkLED(11, 0.5)

if __name__ == "__main__":
    main()

