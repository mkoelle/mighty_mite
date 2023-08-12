import math
from machine import Pin
from time import sleep
from lib.sensor.ultrasonic_hcsr04 import UltrasonicSensor
from lib.servo.mg995 import Servo
from lib.stepper.uln2003 import Stepper, HALF_STEP, FULL_STEP

led = Pin(2, Pin.OUT)
range_sensor = UltrasonicSensor(trigger_pin=15,echo_pin=16,echo_timeout_us=10000)
motor = Servo(pin=13)
stepper = Stepper( mode=HALF_STEP, pin1=2, pin2=0, pin3=4, pin4=5 ,delay=10)

FORWARD = 1
BACKWARD = -1

direction = FORWARD

while True:
    distance = range_sensor.distance_cm()
    degrees = math.floor(120 - 120*(distance/100))
    print('Distance, degrees: [', '{: >3}'.format(distance), ', ', '{: >4}'.format(degrees), ']')
    if(distance>0):
        motor.move(degrees)
    stepper.step(1,1)
        