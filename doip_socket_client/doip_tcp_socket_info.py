import queue

class SocketInfo:

    def __new__(cls):
        if not hasattr(cls, '_socket_instance'):
            cls._socket_instance = super().__new__(cls)
        return cls._socket_instance

    def __init__(self):
        if not hasattr(self, 'socket_dict'):
            self.socket_dict = {}
            self.tcp_sockets_dict = {}
            self.socket_que = queue.Queue()

    def update_socket(self,
                      _socket_hash,
                      socket_status,
                      _tcp_socket):

        if socket_status == -1:
            del self.socket_dict[_socket_hash]
            del self.socket_dict[_socket_hash]
        else:
            self.socket_dict[_socket_hash] = socket_status
            self.tcp_sockets_dict[_socket_hash] = _tcp_socket
            print(self.socket_dict, socket_status)

    def does_socket_exist(self,
                          _socket_hash):
        return _socket_hash in self.tcp_sockets_dict

    def get_socket_status(self):
        return len(self.socket_dict.items())