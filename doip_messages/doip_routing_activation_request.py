
from doip.doip_message import DoipMessage
from utils_constants.doip_constants import DoipMsgTypes

class RoutingActivationRequest(DoipMessage):
    def __init__(self, src_address: int,
                 activation_type: int,
                 reserved_by_iso: int):
        super().__init__(
            DoipMsgTypes.RoutingActivationRequest.value,
            src_address=src_address,
            activation_type=activation_type,
            reserved_by_iso=reserved_by_iso
        )