import serial
import select
import signal
import time


class InstrumentBase(serial.Serial):
    """
    InstrumentBase

    Keyword argument:
    port:               Serial port
    baudrate:           Baud rate
    bytesize:           Number of data bits
    parity:             Parity check setting
    stopbits:           Number of stop bits
    timeout:            Read timeout
    xonxoff:            Software flow control
    rtscts:             RTS/CTS hardware flow control
    dsrdtr:             DSR/DTR hardware flow control
    writeTimeout:       Write timeout
    interCharTimeout:   Inter-character timeout

    Exceptions:
    ValueError:         Out-of-range parameters
    SerialException:    Device cannot be found or configured
    """

    def __init__(self, *args, **kwargs):
        self.buffer_size = kwargs.pop('buffer_size', 4096)
        self.line_ending = kwargs.pop('line_ending', '\n')
        super(InstrumentBase, self).__init__(*args, **kwargs)

    def send(self, command):
        """
        send

        Parameters:
        command:    Command to send to instrument
        """
        self.write(command + self.line_ending)

    def query(self, command):
        """
        Send a command to an instrument and return the response

        Parameters:
        command:    Command to send to the instrument

        Return:
        Response from instrument
        """
        self.send(command)
        return self.readline().strip()

