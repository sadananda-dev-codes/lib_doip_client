
from utils_constants.doip_utils import *
from doip_socket_client.doip_tcp_socket_info import SocketInfo
import socket
from typing import Dict

class DoipTcpSocket(socket.socket):

    def connection_status(self):
        SocketInfo().update_socket(id(self), self.fileno())

    def close(self):
        super().close()
        SocketInfo().update_socket(id(self), self.fileno())

class DoipTcpClient:

    def __init__(self):
        self._client_socket = None
        self._client_ip_endpoint = None
        self._server_ip_endpoint = None

    def doip_open_tcp_socket(self):

        if self._client_socket is None:
            self._client_socket = DoipTcpSocket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            assert '[error] socket is already open'
            return self

    def doip_bind_to_socket(self,
                            **client_ip_endpoint: Dict):

        assert self._client_socket is not None, '[Error] Socket already open — close it before opening a new one'
        self._client_ip_endpoint = client_ip_endpoint
        self._client_socket.bind(tuple(self._client_ip_endpoint.values()))

    def doip_connect_server(self,
                            **server_ip_endpoint: Dict):

        assert self._client_ip_endpoint is not None, '[error] [client socket] should be bind to valid ip'

        _hash = calculate_hash(server_ip_endpoint.values())
        if not SocketInfo().does_socket_exist(_hash):

            SocketInfo().update_socket(_hash,
                                       self._client_socket.fileno(),
                                       self._client_socket)
            self._server_ip_endpoint = server_ip_endpoint

            try:
                print(self._server_ip_endpoint)
                self._client_socket.connect(tuple(self._server_ip_endpoint.values()))
                return True
            except socket.gaierror:
                print("Invalid IP address or hostname")
            except socket.timeout:
                print("Connection timed out")
            except ConnectionRefusedError:
                print("Target machine refused connection")
            except OSError as e:
                print(f"OS error: {e}")
        else:
            raise DoipException('Socket Already Exists')

    def doip_connect_close_connection(self):
        self._client_socket.close()

    def doip_socket_info(self):
        print(f'{self.ip_endpoint}')

    def doip_status(self):
        return self._client_socket.fileno()

    def doip_send_data(self,
                       data: str):
        self._client_socket.sendall(data)
