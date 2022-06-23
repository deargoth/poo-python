import re

def verify_type(value):
    if isinstance(value, str):
        value = re.sub(r'[^0-9]', '', value)
    
    return value