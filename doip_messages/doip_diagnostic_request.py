
from doip.doip_message import DoipMessage
from constants.doip_constants import DoipMsgTypes

class DiagnosticMessage(DoipMessage):
    def __init__(self, source_address, target_address, user_data):
        super().__init__(
            DoipMsgTypes.DiagnosticMessage.value,
            source_address=source_address,
            target_address=target_address,
            user_data=user_data
        )