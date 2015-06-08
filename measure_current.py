#!/usr/local/bin/python

import sys
import time

import instrument
from instrument import AgilentE3632A

def main():
    try:
        dc_supply = AgilentE3632A(port='/dev/cu.usbserial', timeout=5)

        print "Checking to see if the instrument is connected..."
        if not dc_supply.is_connected():
            print "ERROR: Instrument is not connected"
            sys.exit(1)

        print "Putting instrument in remote mode..."
        dc_supply.set_remote()

        print "Resetting instrument..."
        dc_supply.reset()

        print "Setting voltage protection level..."
        dc_supply.set_voltage_protection_level(3.5)

        print "Setting voltage protection state..."
        dc_supply.set_voltage_protection_state('ON')

        print "Setting current protection level..."
        dc_supply.set_current_protection_level(2.0)

        print "Setting current protection state..."
        dc_supply.set_current_protection_state('ON')

        print "Setting voltage..."
        dc_supply.set_voltage(3.0)

        print "Getting output state..."
        if not dc_supply.get_output_state():
            print "Setting output state to ON..."
            dc_supply.set_output_state(instrument.ON)
            print "Getting output state..."
            if not dc_supply.get_output_state():
                print "ERROR: Could not set output state to ON"
                sys.exit(1)

        print "Getting current level..."
        while True:
            print dc_supply.measure_current()

    except KeyboardInterrupt:
        print "Exiting due to keyboard interrupt"
        dc_supply.readline()
        dc_supply.set_output_state(instrument.OFF)
        dc_supply.set_local()
        dc_supply.close()


if __name__ == '__main__':
        main()


