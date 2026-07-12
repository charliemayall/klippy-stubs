from _typeshed import Incomplete

message_shutdown: str
message_protocol_error1: str
message_protocol_error2: str
message_mcu_connect_error: str
Common_MCU_errors: Incomplete

def error_hint(msg): ...

class PrinterMCUError:
    printer: Incomplete
    clarify_callbacks: Incomplete
    def __init__(self, config) -> None: ...
    def add_clarify(self, msg, callback) -> None: ...

def load_config(config): ...
