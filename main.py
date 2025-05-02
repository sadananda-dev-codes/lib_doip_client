from doip_messages.doip_diagnostic_request import DiagnosticMessage
from doip_messages.doip_routing_activation_request import RoutingActivationRequest

msg1 = RoutingActivationRequest(0x3285, 10, 0)
print(msg1)
print("Packed:", msg1.pack())

print("\n")

msg2 = DiagnosticMessage(0x3285, 0x5600, [85, 32, 65, 0, 15, 96, 32, 0, 70, 3, 9, 6])
print(msg2)
print("Packed:", msg2.pack())

msg3 = DiagnosticMessage(0x3285, 0x5600, [31, 1, 2, 2])
print(msg3)
print("Packed:", msg3.pack())

msg4 = DiagnosticMessage(0x3285, 0x5600, [31, 3, 2, 2, 0xF0, 0, 98])
print(msg4)
print("Packed:", msg4.pack())
