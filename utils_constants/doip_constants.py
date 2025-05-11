from enum import IntEnum

class DoipMsgTypes(IntEnum):
    GenericDoIPNegativeAcknowledge = 0x0000
    VehicleIdentificationRequest = 0x0001
    VehicleIdentificationRequestWithEID = 0x0002
    VehicleIdentificationRequestWithVIN = 0x0003
    RoutingActivationRequest = 0x0005
    AliveCheckRequest = 0x0007
    DoipEntityStatusRequest = 0x4001
    DiagnosticPowerModeRequest = 0x4003
    DiagnosticMessage = 0x8001

DOIP_MESSAGE_DEFINITIONS = {
    DoipMsgTypes.RoutingActivationRequest: {
        "format": ">BBHIHBI",
        "length": 11,
        "fields": ["payload_type", "src_address", "activation_type", "reserved_by_iso"]
    },
    DoipMsgTypes.DiagnosticMessage: {
        "format": ">BBHIHH",
        "length": 4,
        "fields": ["payload_type", "source_address", "target_address", "user_data"]
    },
}