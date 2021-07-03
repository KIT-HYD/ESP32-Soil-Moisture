# ESP32-Soil-Moisture
MicroPython ESP32 based Soil Moisture Sensor Node

## Install 

You can add the `sm.py` library file to your MicroPython project. 
The `main.py` is a simple and straightforward implementation 
of `sm.py` for demonstration but should be replaced with your 
actual project file.

For working with the files, you will need the development dependencies.
These can be installed like:

```bash
pip install -r dev-requirements.txt
```

## Install MicroPython

Download a MicroPython for the ESP32: https://micropython.org/download/esp32/

Rename the file to `esp32.bin`.

Connect the device and erase the flash:

```bash
esptool.py --chip esp32 --port <PORT> erase_flash
```

Then upload MicroPython to the device

```bash
esptool.py --chip esp32 --port <PORT> --baud 460800 write_flash -z 0x1000 esp32.bin
```

The `<PORT>` has to be replaced by the port where the device is connected. On Linux that
is typically something like `/dev/ttyUSB0` (you can ls the /dev/tty*), on Windows its
one of the `COM`, like `COM3`.

If you run into communication errors, you can choose a slower baud rate like 115200

## upload programm

First, rename `sm_config.json.example` to `sm_config.json` and adjust the file content to your
needs.
You can use an IDE like thonny (`pip install thonny`) to upload the files, or `ampy`:

You can copy all firmware files to your board like:

```bash
ampy --port <PORT> put ./src/*
```

**Important**: That will also copy the `boot.py` and `main.py` over and repalce existing files!
The minimum required files are the `sm.py` and its configuration in `sm_config.json`.
You can add (or upgrade) them like:

```bash
ampy put --port <PORT> put src/sm.py
ampy put --port <PORT> put src/sm_config.json
```