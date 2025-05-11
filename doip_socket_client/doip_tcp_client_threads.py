import threading
import time
from doip_tcp_socket_info import SocketInfo

class doip_tcp_client_send_req(threading):
    
    def __init__(self,
                 socket):
        super().__init__(self)
        self._socket = socket

    def run(self):

        while SocketInfo().is_any_socket_alive():
            _request = SocketInfo().socket_que.get()
            self.doip_send_to(_request)

    def doip_send_to(self,
                     doip_request):
            self._socket.send(doip_request)

class doip_tcp_client_receive_req(threading):

    def __init__(self):
        super().__init__(self)
        self.daemon = True

    def run(self):
        while SocketInfo().is_any_socket_alive():
            ##keeping polling
            pass