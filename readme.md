# mighty might

microprocessors for fun

## Dev setup

- python 3
    - pyenv for python version managment
    - [poetry](https://python-poetry.org/docs/) for package management
    - [CH341 serial drivers](https://github.com/juliagoda/CH341SER#tutorial-on-ubuntu)
- tio - a simple serial device I/O tool
    - [tio installation](https://github.com/tio/tio#4-installation)

## Dev flow

```sh
# install the supported python version
pyenv install

# launch the local virtual env
poetry shell

# install the project dependencies
poetry install
```

```sh
# listing devices
tio -L

# connecting to serial
tio /dev/ttyUSB0
# is the same as:
tio -b 115200 -d 8 -f none -s 1 -p none /dev/ttyUSB0
```

```sh
# list all deployed files
ampy --port /dev/ttyUSB0 --baud 115200 ls
# deploy
ampy --port /dev/ttyUSB0 --baud 115200 put src/ .
## Remember to restart the board
```

## Flashing a new chip

```sh
curl https://micropython.org/resources/firmware/esp8266-20230426-v1.20.0.bin --output esp8266.bin
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dout 0 esp8266.bin
```

### chip not showing up?

```sh
#remove brltty - 
sudo apt-get purge --auto-remove brltty
```

### unable to connect to serial monitor?

```sh
# The initial baud rate of the chip is 74880
# use this rate to see boot messages, usefull if stuck in boot loop
tio -b 74880 -d 8 -f none -s 1 -p none /dev/ttyUSB0 | tee serial.log
```

## Resources

- [Awesome ESP](https://github.com/agucova/awesome-esp)
- [MicroWebSrv2](https://github.com/jczic/MicroWebSrv2)
- Message Queuing Telemetry Transport (MTTQ)
    - [What is MQTT and How It Works](https://randomnerdtutorials.com/what-is-mqtt-and-how-it-works/)
    - [MicroPython – Getting Started with MQTT on ESP32/ESP8266](https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/)
