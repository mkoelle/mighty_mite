import math
from machine import Pin
import network
import ujson
import sys

# from time import sleep
from lib.sensor.ultrasonic_hcsr04 import UltrasonicSensor
from lib.servo.mg995 import Servo
from lib.stepper.uln2003 import Stepper, HALF_STEP  # , FULL_STEP


import uasyncio as asyncio
from lib.web.nanoweb import Nanoweb

naw = Nanoweb(80)
naw.STATIC_DIR = "www"
naw.INDEX_FILE = "www/index.html"


wlan_ap = network.WLAN(network.AP_IF)
wlan_sta = network.WLAN(network.STA_IF)


# Declare route directly with decorator
@naw.route("/ping")
async def ping(request):
    await request.write("HTTP/1.1 200 OK\r\n\r\n")
    await request.write("Content-Type: text/html\r\n")
    await request.write("pong")


@naw.route("/networks")
async def list_wifi_networks(request):
    try:
        wlan_sta.active(True)
        networks = wlan_sta.scan()

        AUTHMODE = {0: "open", 1: "WEP", 2: "WPA-PSK", 3: "WPA2-PSK", 4: "WPA/WPA2-PSK"}
        network_list = [
            {
                "ssid": info[0].decode('utf-8'),
                "channel": info[2],
                "signal_strength": info[3],
                "security": AUTHMODE.get(info[4], '?') 
            } 
            for info in networks
        ]
        
        response = ujson.dumps({"networks": network_list})

        await request.write("HTTP/1.1 200 OK\r\n\r\n")
        await request.write("Content-Type: application/json\r\n")
        # await request.write(f"Content-Length: {len(response.encode('utf-8'))}\r\n")
        await request.write( response )
    except OSError as e:
        print("exception", str(e))
        await request.write("HTTP/1.1 500 ERR\r\n\r\n")
        await request.write("Content-Type: text/strings\r\n")
        await request.write( str(e))

loop = asyncio.get_event_loop()
loop.create_task(naw.run())
loop.run_forever()

led = Pin(2, Pin.OUT)
range_sensor = UltrasonicSensor(trigger_pin=15, echo_pin=16, echo_timeout_us=10000)
motor = Servo(pin=13)
stepper = Stepper(mode=HALF_STEP, pin1=2, pin2=0, pin3=4, pin4=5, delay=10)

FORWARD = 1
BACKWARD = -1

direction = FORWARD

while True:
    distance = range_sensor.distance_cm()
    degrees = math.floor(120 - 120 * (distance / 100))
    print(
        "Distance, degrees: [",
        "{: >3}".format(distance),
        ", ",
        "{: >4}".format(degrees),
        "]",
    )
    if distance > 0:
        motor.move(degrees)
    stepper.step(1, 1)
