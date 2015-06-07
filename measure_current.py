#!/usr/local/bin/python

import sys
import time

from agilent_E3632A import AgilentE3632A

def main():
    try:
        instrument = AgilentE3632A(port='/dev/cu.usbserial', timeout=5)

        print "Putting instrument in remote mode..."
        instrument.set_remote()

        print "Resetting instrument..."
        instrument.reset()

        print "Setting voltage protection level..."
        instrument.set_voltage_protection_level(3.5)

        print "Setting voltage protection state..."
        instrument.set_voltage_protection_state('ON')

        print "Setting current protection level..."
        instrument.set_current_protection_level(2.0)

        print "Setting current protection state..."
        instrument.set_current_protection_state('ON')

        print "Setting voltage..."
        instrument.set_voltage(3.0)

        print "Getting output state..."
        result = instrument.get_output_state()
        if '1' != result:
            print "Setting output state to ON..."
            instrument.set_output_state('ON')
            print "Getting output state..."
            result = instrument.get_output_state()
            if '1' != result:
                print "ERROR: Could not set output state to ON"
                sys.exit(1)

        print "Getting current level..."
        while True:
            print instrument.measure_current()

    except KeyboardInterrupt:
        print "Exiting due to keyboard interrupt"
        instrument.readline()
        instrument.set_local()
        instrument.close()


if __name__ == '__main__':
        main()


