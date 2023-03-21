import RPi.GPIO as GPIO
import time

def blinkLED(pin, delay):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(delay)

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)

    while True:
        # Test 1: blink LED 5 times w on/off intervals 500ms
        for i in range(5):
            blinkLED(11, 0.5)

        # Test 2: read output of light sensor w intervals 100 ms
        # print raw value & "light" or "dark" w threshold 10


        # Test 3: blink LED 4 times w on/off intervals 200 ms
        for i in range(4):
            blinkLED(11, 0.2)

        # Test 4: read output of sound sensor w intervals 100 ms
        # print raw value 
        # if tapped, LED turns on for 100 ms
            

if __name__ == "__main__":
    main()

