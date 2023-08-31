import math
from machine import Pin, I2C
import uasyncio as asyncio
import network
import ujson
import sys

# from time import sleep
from lib.sensor.ultrasonic_hcsr04 import UltrasonicSensor
from lib.servo.mg995 import Servo
from lib.stepper.uln2003 import Stepper, HALF_STEP  # , FULL_STEP
from lib.web.nanoweb import Nanoweb
from lib.display.ssd1306 import SSD1306_I2C

naw = Nanoweb(80)
naw.STATIC_DIR = "www"
naw.INDEX_FILE = "www/index.html"


wlan_ap = network.WLAN(network.AP_IF)
wlan_sta = network.WLAN(network.STA_IF)

# Pin Configuration
LED_PIN = 2
LASER_PIN = 0
led = Pin(LED_PIN, Pin.OUT)
laser = Pin(LASER_PIN, Pin.OUT)


# OLED Display Configuration
WIDTH = 128
HEIGHT = 64
I2C_SCL_PIN = 5
I2C_SDA_PIN = 4

# Initialize the I2C bus and OLED display
i2c = I2C(scl=Pin(I2C_SCL_PIN), sda=Pin(I2C_SDA_PIN))
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)


async def display_task():
    seconds = 0

    while True:
        # Clear the display
        oled.fill(0)

        # Set the text properties
        x = 0
        y = 0

        # Draw the first line on the display
        oled.text("Hello, World!", x, y)

        # Draw the second line on the display (counting seconds)
        oled.text("Seconds: {}".format(seconds), x, y + 10)

        # Refresh the display
        oled.show()

        # Update the seconds counter
        print(f"i've been on for {seconds} seconds")

        # Update the seconds counter
        seconds += 1
        # Wait for 1 second
        await asyncio.sleep(1)


async def flash_led():
    while True:
        # Turn on the LED
        led.on()
        laser.on()
        await asyncio.sleep(1)  # Wait for 1 second

        # Turn off the LED
        led.off()
        laser.off()
        await asyncio.sleep(1)  # Wait for 1 second


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
        await request.write(response)
    except OSError as e:
        print("exception", str(e))
        await request.write("HTTP/1.1 500 ERR\r\n\r\n")
        await request.write("Content-Type: text/strings\r\n")
        await request.write(str(e))


tasks = [flash_led(), naw.run(), display_task()]
# Run the asyncio tasks forever


async def main():
    while True:
        await asyncio.gather(*tasks)

asyncio.run(main())


# loop = asyncio.get_event_loop()
# loop.create_task(naw.run())
# loop.run_forever()

# led = Pin(2, Pin.OUT)
# range_sensor = UltrasonicSensor(trigger_pin=15, echo_pin=16, echo_timeout_us=10000)
# motor = Servo(pin=13)
# stepper = Stepper(mode=HALF_STEP, pin1=2, pin2=0, pin3=4, pin4=5, delay=10)

# FORWARD = 1
# BACKWARD = -1

# direction = FORWARD

# while True:
#     distance = range_sensor.distance_cm()
#     degrees = math.floor(120 - 120 * (distance / 100))
#     print(
#         "Distance, degrees: [",
#         "{: >3}".format(distance),
#         ", ",
#         "{: >4}".format(degrees),
#         "]",
#     )
#     if distance > 0:
#         motor.move(degrees)
#     stepper.step(1, 1)
