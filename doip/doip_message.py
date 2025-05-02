import struct
from constants.doip_constants import DOIP_MESSAGE_DEFINITIONS, DoipMsgTypes

class DoipMessage:
    def __init__(self, payload_type, **kwargs):
        self.payload_type = payload_type
        self.header = {
            'protocol_version': 0x02,
            'inverse_protocol_version': 0xFD,
            'payload_type': payload_type,
            'payload_length': 0
        }
        self.payload_fields = kwargs
        self.definition = DOIP_MESSAGE_DEFINITIONS.get(DoipMsgTypes(payload_type), {})
        self.update_payload_length()

    def update_payload_length(self):
        self.header['payload_length'] = self.definition.get('length', 0)
        if 'user_data' in self.payload_fields:
            self.header['payload_length'] += len(self.payload_fields['user_data'])

    def pack(self):
        buffer = bytearray(1400)
        format = self.definition.get('format', 0)
        _h = list(self.header.values())
        _v = list(self.payload_fields.values())

        if 'user_data' in self.payload_fields:
            format = format + str(self.header['payload_length']-self.definition.get('length', 0)) + 'B'
            _v = [*_v[:-1], *_v[-1]]
        struct.pack_into(format, buffer, 0, *_h, *_v)
        return buffer[:struct.calcsize(format)].hex()

    def __str__(self):
        combined = {**self.header, **self.payload_fields}
        return '\n'.join(f"{k}: {v}" for k, v in combined.items())