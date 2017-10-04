import RPi.GPIO as GPIO
from time import sleep
from pygame import mixer
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)

try:
    while(True):
        GPIO.add_event_detect(29, GPIO.BOTH)
        def my_callback(channel):
            GPIO.output(36, GPIO.input(29))
        GPIO.add_event_callback(29, my_callback)

except KeyboardInterrupt:
        print("quitting")
GPIO.cleanup()
