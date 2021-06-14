import RPi.GPIO as GPIO
import time
import logging


def boot():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT)
    GPIO.setwarnings(False)

    GPIO.output(37, True)


    GPIO.output(37, False)
    time.sleep(.1)
    GPIO.output(37, True)
    time.sleep(.1)


    GPIO.cleanup()


if __name__ == "__main__":
    boot()