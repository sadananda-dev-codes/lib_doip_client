from doip_messages.doip_diagnostic_request import DiagnosticMessage
from doip_messages.doip_routing_activation_request import RoutingActivationRequest
from doip_socket_client import doip_tcp_socket_client
from doip_socket_client.doip_tcp_socket_client import DoipTcpClient

msg1 = RoutingActivationRequest(0x3285, 10, 0)
msg2 = DiagnosticMessage(0x3285, 0x5600, [85, 32, 65, 0, 15, 96, 32, 0, 70, 3, 9, 6])
msg3 = DiagnosticMessage(0x3285, 0x5600, [31, 1, 2, 2])
msg4 = DiagnosticMessage(0x3285, 0x5600, [31, 3, 2, 2, 0xF0, 0, 98])

d_tcp = DoipTcpClient()
d_tcp.doip_open_tcp_socket()
d_tcp.doip_bind_to_socket(ENDPOINT_IP='127.0.0.51', ENDPOINT_PORT=51)
d_tcp.doip_connect_server(ENDPOINT_IP='127.0.0.32', ENDPOINT_PORT=32)
d_tcp.doip_send_data(msg1.pack().encode('utf-8'))
d_tcp.doip_send_data(msg2.pack().encode('utf-8'))
d_tcp.doip_send_data(msg3.pack().encode('utf-8'))
d_tcp.doip_send_data(msg4.pack().encode('utf-8'))
d_tcp.doip_send_data('3285'.encode('utf-8'))

t_tcp_1 = DoipTcpClient()
t_tcp_1.doip_open_tcp_socket()
t_tcp_1.doip_bind_to_socket(ENDPOINT_IP='127.0.0.56', ENDPOINT_PORT=56)
t_tcp_1.doip_connect_server(ENDPOINT_IP='127.0.0.85', ENDPOINT_PORT=85)
t_tcp_1.doip_send_data(msg1.pack().encode('utf-8'))
t_tcp_1.doip_send_data(msg2.pack().encode('utf-8'))
t_tcp_1.doip_send_data(msg3.pack().encode('utf-8'))
t_tcp_1.doip_send_data(msg4.pack().encode('utf-8'))
t_tcp_1.doip_send_data('3285'.encode('utf-8'))

while True:
    pass