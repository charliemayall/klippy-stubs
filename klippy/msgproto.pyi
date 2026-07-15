from collections.abc import Callable
from typing import Any, TypeVar, overload

DefaultMessages: list[tuple[str, str]]
MESSAGE_MIN: int
MESSAGE_MAX: int
MESSAGE_HEADER_SIZE: int
MESSAGE_TRAILER_SIZE: int
MESSAGE_POS_LEN: int
MESSAGE_POS_SEQ: int
MESSAGE_TRAILER_CRC: int
MESSAGE_TRAILER_SYNC: int
MESSAGE_PAYLOAD_MAX: int
MESSAGE_SEQ_MASK: int
MESSAGE_DEST: int
MESSAGE_SYNC: int

class error(Exception): ...

def crc16_ccitt(buf: bytes | bytearray) -> int: ...

class PT_uint32:
    is_int: bool
    is_dynamic_string: bool
    max_length: int
    signed: bool
    def encode(self, out: bytearray, v: int) -> None: ...
    def parse(self, s: bytes, pos: int) -> tuple[int, int]: ...

class PT_int32(PT_uint32):
    signed: bool

class PT_uint16(PT_uint32):
    max_length: int

class PT_int16(PT_int32):
    signed: bool
    max_length: int

class PT_byte(PT_uint32):
    max_length: int

class PT_string:
    is_int: bool
    is_dynamic_string: bool
    max_length: int
    def encode(self, out: bytearray, v: str | bytes) -> None: ...
    def parse(self, s: bytes, pos: int) -> tuple[bytes, int]: ...

class PT_progmem_buffer(PT_string): ...
class PT_buffer(PT_string): ...

class enumeration_error(error):
    enum_name: str
    value: int
    def __init__(self, enum_name: str, value: int) -> None: ...
    def get_enum_params(self) -> dict[str, int]: ...

class Enumeration:
    is_int: bool
    is_dynamic_string: bool
    pt: PT_uint32
    max_length: int
    enum_name: str
    enums: dict[str, int]
    reverse_enums: dict[int, str]
    def __init__(
        self, pt: PT_uint32, enum_name: str, enums: dict[str, int]
    ) -> None: ...
    def encode(self, out: bytearray, v: str) -> None: ...
    def parse(self, s: bytes, pos: int) -> tuple[str, int]: ...

MessageTypes: dict[str, type]

def lookup_params(
    msgformat: str, enumerations: dict[str, dict[str, int]] = {}
) -> list[tuple[str, Any]]: ...
def lookup_output_params(msgformat: str) -> list[Any]: ...
def convert_msg_format(msgformat: str) -> str: ...

class MessageFormat:
    msgid_bytes: bytes
    msgformat: str
    debugformat: str
    name: str
    param_names: list[tuple[str, Any]]
    param_types: list[Any]
    name_to_type: dict[str, Any]
    def __init__(
        self,
        msgid_bytes: bytes,
        msgformat: str,
        enumerations: dict[str, dict[str, int]] = {},
    ) -> None: ...
    def encode(self, params: list[Any]) -> bytes: ...
    def encode_by_name(self, **params: Any) -> bytes: ...
    def parse(self, s: bytes, pos: int) -> tuple[dict[str, Any], int]: ...
    def format_params(self, params: dict[str, Any]) -> str: ...

class OutputFormat:
    name: str
    msgid_bytes: bytes
    msgformat: str
    debugformat: str
    param_types: list[Any]
    def __init__(self, msgid_bytes: bytes, msgformat: str) -> None: ...
    def parse(self, s: bytes, pos: int) -> tuple[list[Any], int]: ...
    def format_params(self, params: list[Any]) -> str: ...

class UnknownFormat:
    name: str
    def parse(self, s: bytes, pos: int) -> tuple[dict[str, Any], int]: ...
    def format_params(self, params: dict[str, Any]) -> str: ...

_T = TypeVar("_T")
_U = TypeVar("_U")

class MessageParser:
    error = error
    warn_prefix: str
    unknown: UnknownFormat
    enumerations: dict[str, dict[str, int]]
    messages: list[MessageFormat]
    messages_by_id: dict[int, MessageFormat]
    messages_by_name: dict[str, MessageFormat]
    msgid_by_format: dict[str, int]
    msgid_parser: PT_int32
    config: dict[str, Any]
    version: str
    raw_identify_data: str
    def __init__(self, warn_prefix: str = "") -> None: ...
    def check_packet(self, s: bytes) -> int: ...
    def dump(self, s: bytes) -> str: ...
    def format_params(self, params: dict[str, Any]) -> str: ...
    def parse(self, s: bytes) -> dict[str, Any]: ...
    def encode_msgblock(self, seq: int, cmd: bytes) -> bytes: ...
    def lookup_command(self, msgformat: str) -> MessageFormat: ...
    def lookup_msgid(self, msgformat: str) -> int: ...
    def create_command(self, msg: str) -> bytes: ...
    def create_dummy_response(
        self, msgname: str, params: dict[str, Any] = {}
    ) -> bytes: ...
    def fill_enumerations(self, enumerations: dict[str, dict[str, int]]) -> None: ...
    build_versions: list[str]
    def process_identify(self, data: bytes, decompress: bool = True) -> None: ...
    def get_raw_data_dictionary(self) -> bytes: ...
    def get_version_info(self) -> tuple[str, list[str]]: ...
    def get_messages(self) -> list[MessageFormat]: ...
    def get_enumerations(self) -> dict[str, dict[str, int]]: ...
    def get_constants(self) -> dict[str, Any]: ...
    class sentinel: ...

    # hand-refined: mcu constant getters with sentinel default
    @overload
    def get_constant(
        self,
        name: str,
        default: type[sentinel] = ...,
        parser: Callable[[str], _U] = ...,
    ) -> _U: ...
    @overload
    def get_constant(
        self, name: str, default: _T, parser: Callable[[str], _U] = ...
    ) -> _U | _T: ...
    @overload
    def get_constant_float(self, name: str, default: type[sentinel] = ...) -> float: ...
    @overload
    def get_constant_float(self, name: str, default: _T) -> float | _T: ...
    @overload
    def get_constant_int(self, name: str, default: type[sentinel] = ...) -> int: ...
    @overload
    def get_constant_int(self, name: str, default: _T) -> int | _T: ...
