import time


import instrument_base


class AgilentE3632A(instrument_base.InstrumentBase):
    """
    AgilentE3632A
    """
    def __init__(self, *args, **kwargs):
        kwargs['dsrdtr'] = True
        kwargs['timeout'] = 5
        self.command_delay = kwargs.pop('command_delay', 0.500)
        super(AgilentE3632A, self).__init__(*args, **kwargs)
        self.set_remote()

    def command_delay_function(self, command_delay=None):
        if command_delay is not None:
            time.sleep(command_delay)
        else:
            time.sleep(self.command_delay)

    def reset(self):
        self.send('*RST')
        self.command_delay_function(3.0)

    def set_remote(self):
        self.send('system:remote')
        self.command_delay_function()

    def set_local(self):
        self.send('system:local')
        self.command_delay_function()

    def set_output_state(self, value):
        self.send('output %s' % (value))
        self.command_delay_function()

    def get_output_state(self):
        return self.query('output?')

    """
    Voltage methods
    """
    def set_voltage(self, voltage):
        self.send('voltage %s' % (voltage))
        self.command_delay_function()

    def get_voltage(self):
        return self.query('voltage?')

    def set_voltage_protection_level(self, level):
        self.send('voltage:protection:level %s' % (level))
        self.command_delay_function()

    def set_voltage_protection_state(self, state):
        self.send('voltage:protection:state %s' % (state))
        self.command_delay_function()

    """
    Current methods
    """
    def set_current(self, current):
        self.send('current %s' % (current))
        self.command_delay_function()

    def get_current(self):
        return self.query('current?')

    def set_current_protection_level(self, level):
        self.send('current:protection:level %s' % (level))
        self.command_delay_function()

    def set_current_protection_state(self, state):
        self.send('current:protection:state %s' % (state))
        self.command_delay_function()

    """
    Measurement methods
    """
    def measure_voltage(self):
        return self.query('measure:voltage?')

    def measure_current(self):
        return self.query('measure:current?')

