#!/usr/bin/python

import serial
import time
import argparse

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('dsmrsim', '../templates'))

template = env.get_template('dsmr-2.2-2ME382')

def create_parser():
    parser = argparse.ArgumentParser(
        description='Run a smart meter simulator compatible with Dutch Smart Meter Requirements'
    )

    parser.add_argument(
        'port', metavar='port', type=str,
        help='Serial port to use'
    )

    parser.add_argument(
        '-v', '--version', type=float, default=2.2, choices=[2.2, 4.0],
        help='DSMR version'
    )

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    try:
        if args.version == 2.2:
            # Connect to serial port at 9600 baud with 7 data bits per byte, no parity checking and 2 stop bits
            serial_port = serial.Serial(args.port, 9600, bytesize=serial.SEVENBITS, parity=serial.PARITY_NONE, stopbits=2)
        else:
            # Connect to serial port at 115200 baud with 8 data bits per byte, no parity checking and 1 stop bit
            serial_port = serial.Serial(args.port, 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=1)

    except serial.SerialException as e:
        print e

    else:
        print "Opened: ", serial_port.name

        while True:
            msg = template.render(the='variables', go='here').encode('ascii')

            print "Send:", msg

            serial_port.write(msg)

            time.sleep(10)

if __name__ == '__main__':
    main()
