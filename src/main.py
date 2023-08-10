import math
from machine import Pin
from time import sleep
from lib.sensor.ultrasonic_hcsr04 import UltrasonicSensor
from lib.servo.mg995 import Servo

led = Pin(2, Pin.OUT)
range_sensor = UltrasonicSensor(trigger_pin=15,echo_pin=16,echo_timeout_us=10000)

motor=Servo(pin=13)

movements = [0,60,120,60,120]

def motor_test(max):
    motor.update_offset(23,max)
    print('offset max: ',max)
    for move in movements:
        print('servo ', move)
        motor.move(move) 
        sleep(.2)

# motor_test(113)

# print('test complete')
# motor.move(0)

# for i in range(10):
#     led.value(1)
#     sleep(0.5)
#     led.value(0)
#     sleep(0.5)


while True:
    distance = range_sensor.distance_cm()
    degrees = math.floor(120 - 120*(distance/100))
    print('Distance, degrees: [', '{: >3}'.format(distance), ', ', '{: >4}'.format(degrees), ']')
    if(distance>0):
        motor.move(degrees)
    sleep(.05)
        