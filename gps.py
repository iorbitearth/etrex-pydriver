#! /usr/bin/env python3


import sys, argparse, traceback, serial, signal


class ETrexDriver(object):
    """ """

    def __init__(self, device, baud=4800, timeout=1):
        """
        Initialize the driver object by configuring/opening serial interface.
        """
        self.path = device
        self.baud = baud
        self.dev = serial.Serial(self.path, self.baud, timeout=timeout)
        self.encoding = "utf-8"
        self.running = False
        self.numpkts = 0

        # register ctrl-c signal handler
        signal.signal(signal.SIGINT, self.signal_handler)


    def __del__(self):
        """
        Cleanup driver resources.
        """
        self.dev.close()
        self.__dump_metrics()


    def __dump_metrics(self):
        """
        Print out useful metrics.
        """
        print ("\n\n===== Metrics/Stats =====")
        print ("number of packets received: " + str(self.numpkts))



    def signal_handler(self, signal, frame):
        """
        Handle the Ctrl-C UNIX signal to shutdown the applcation.
        """
        print("\n\nReceived signal" + str(signal) + ": shutting down etrex driver...")
        self.running = False


    def __process_data(self, data):
        """
        Process raw GPS ascii data into something more meaningful.
        """


    def run(self):
        """
        Beginning processing GPS data indefinitely.
        """
        self.running = True
        data = ""

        while self.running:
            try:
                # read GPS bytes up to first newline character
                data = self.dev.readline()

                # decode the bytes literal
                data = str(data, encoding=self.encoding)

                # display raw ascii data to stdout
                print ("GPS data: " + str(data))

                # increment metrics
                self.numpkts += 1


            except Exception as e:
                print ("ERROR: " + str(e))




def main(argv=None):
    """ main entry point """

    device, baud = parse_args()

    try:
        gps = ETrexDriver(device, baud)
        gps.run()


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

