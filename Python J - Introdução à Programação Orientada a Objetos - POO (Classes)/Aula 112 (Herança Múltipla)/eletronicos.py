from distutils.log import error, info
from log import LogMixin

class Eletronic(LogMixin):
    def __init__(self, name):
        self.name = name
        self.on = False

    def turn_on(self):
        if self.on:
            error = "The device it's already on."
            print(error)
            self.log_error(error)
            return

        self.on = True
        info = "The device it's on now."
        self.log_info(info)
        print(info)

    def turn_off(self):
        if not self.on:
            error = "The device it's already off."
            print(error)
            self.log_error(error)
            return
        self.on = False
        info = "The device it's off now."
        self.log_info(info)
        print(info)