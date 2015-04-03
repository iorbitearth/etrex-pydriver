# etrex-pydriver
Simple python driver for etrex GPS unit

### Usage
Execute the application to view the usage details:
```
$ ./gps -h
usage: gps.py [-h] [-b BAUD] device

Read serial data from an etrex GPS unit

positional arguments:
  device                Path to GPS device file

optional arguments:
  -h, --help            show this help message and exit
  -b BAUD, --baud BAUD  Baud rate (optional, 4800 default)

```

Specify the path to serial device file to read and display GPS data:
```
$ ./gps /dev/ttyUSB0
```

### Dependencies

Install python3 to your system and use pip to install the following dependencies:
* argparse
* pyserial
