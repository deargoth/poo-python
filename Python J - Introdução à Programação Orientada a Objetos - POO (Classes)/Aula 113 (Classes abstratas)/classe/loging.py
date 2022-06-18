class LogMixin:
    def write(self, msg):
        with open('log.log', 'a+') as file:
            file.write(msg)
            file.write(f'\n')
            
    def log_info(self, msg):
        self.write(f'INFO ({self.__class__.__name__}): {msg}')
        
    def log_error(self, msg):
        self.write(f'ERROR ({self.__class__.__name__}): {msg}')