# mighty might

microprocessors for fun

## Dev setup

- python 3
    - pyenv for python version managment
    - [poetry](https://python-poetry.org/docs/) for package management
    - [CH341 serial drivers](https://github.com/juliagoda/CH341SER#tutorial-on-ubuntu)

## Dev flow

```sh
# launch the local virtual env
poetry shell
```

## Flashing a new chip

```sh
curl https://micropython.org/resources/firmware/esp8266-20230426-v1.20.0.bin --output esp8266.bin
esptool.py --chip esp8266 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x0 esp8266.bin
```

### chip not showing up?

```
#remove brltty - 
sudo apt-get purge --auto-remove brltty
```

## Resources

- [Awesome ESP](https://github.com/agucova/awesome-esp)
- [MicroWebSrv2](https://github.com/jczic/MicroWebSrv2)
- Message Queuing Telemetry Transport (MTTQ)
    - [What is MQTT and How It Works](https://randomnerdtutorials.com/what-is-mqtt-and-how-it-works/)
    - [MicroPython – Getting Started with MQTT on ESP32/ESP8266](https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/)
