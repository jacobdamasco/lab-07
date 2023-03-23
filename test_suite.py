import RPi.GPIO as GPIO
import Adafruit_MCP3008
import time

def blinkLED(pin, delay):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(delay)

def readLightSensor(mcp):
    sensorVal = mcp.read_adc(0)
    if (sensorVal > 10):
        print(sensorVal, ", bright")
    else:
        print(sensorVal, ", dark")
    # delay for 100 ms
    time.sleep(.1)


def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    CLK = 23
    MISO = 21
    MOSI = 19
    CS = 24
    mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

    while True:
        # Test 1: blink LED 5 times w on/off intervals 500ms
        for i in range(5):
            blinkLED(11, 0.5)

        # Test 2: read output of light sensor w intervals 100 ms
        # print raw value & "light" or "dark" w threshold 10
        # so run for 50 times in a for loop
        for i in range(50):
            readLightSensor(mcp)


        # Test 3: blink LED 4 times w on/off intervals 200 ms
        for i in range(4):
            blinkLED(11, 0.2)

        # Test 4: read output of sound sensor w intervals 100 ms
        # print raw value 
        # if tapped, LED turns on for 100 ms
            

if __name__ == "__main__":
    main()

