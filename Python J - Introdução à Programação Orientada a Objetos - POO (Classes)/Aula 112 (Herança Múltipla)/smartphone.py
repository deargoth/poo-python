from eletronicos import Eletronic


class Smartphone(Eletronic):
    def __init__(self, name):
        Eletronic.__init__(self, name)
        self.connected = False
    
    def connect(self):
        if not self.on:
            error = "Turn the device on to connect it."
            print(error)
            self.log_error(error)
            return            
        
        if self.connected:
            error = "The device it's already connected to the internet."
            print(error)
            self.log_error(error)
            return

        self.connected = True
        info = "Now the device it's connected to the internet."
        print(info)
        self.log_info(info)
    
    def disconnect(self):
        if not self.connected:
            error = "The device it's already disconnected."
            print(error)
            self.log_error(error)
            return

        self.connected = False
        info = "Now the device it's disconnected."
        print(info)
        self.log_info(info)