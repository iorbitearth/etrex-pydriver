#! /usr/bin/env python3


import sys, argparse, traceback, serial


class ETrexDriver(object):
    """ """

    def __init__(self, device, baud=4800):
        """
        """
        self.path = device
        self.baud = baud
        self.dev = serial.Serial(self.path, self.baud)


    def __del__(self):
        """
        """
        self.dev.close()




def main(argv=None):
    """ main entry point """

    device, baud = parse_args()

    try:
        gps = ETrexDriver(device, baud)


    except Exception as e:
        print ("\ndriver error -- " + format(e) + "\n")
        sys.exit(0)



def parse_args():
    """
    Parse the command line arguments
    """
    parser = argparse.ArgumentParser(description="Read serial data from an etrex GPS unit")
    parser.add_argument("device", help="Path to GPS device file")
    parser.add_argument("-b", "--baud", required=False, default=4800, type=int, help="Baud rate (optional, 4800 default)")
    args = parser.parse_args()

    return (args.device, args.baud)


if __name__ == "__main__":
    sys.exit(main())

