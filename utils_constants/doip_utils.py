import ipaddress
import hashlib

class DoipException(Exception):
    def __init__(self,
                 message = 'invalid doip message'):
        self.msg = message
        super().__init__(self.msg)

class InvalidEndpointException(DoipException):
    def __init__(self,
                 message='Invalid Endpoint Exception'):
        self.msg = message

        super().__init__(self.msg)

def is_valid_ip(_ip,
                _port_no):
    try:
        ipaddress.ip_address(_ip)
        if 0 <= _port_no <= 65535:
            return True
        else:
            return False
    except ValueError:
        return False

def calculate_hash(*args):
    if not args:
        raise ValueError(f'Hash cannot be calculated for {args}')
    joined = "".join(str(arg) for arg in args)
    return hashlib.sha256(joined.encode()).hexdigest()

def check_network_endpoint(ip_endpoint):
    if not is_valid_ip(**ip_endpoint):
        raise InvalidEndpointException('Invalid Endpoint Provided')
    return True
