from . import bus as bus
from _typeshed import Incomplete

I2C_ADDR: int
CMD_MEASURE: Incomplete
CMD_RESET: Incomplete
CMD_INIT_AHT1X: Incomplete
CMD_INIT_AHT2X: Incomplete
STATUS_BUSY: int
STATUS_CALIBRATED: int
MAX_BUSY_CYCLES: int

class AHTBase:
    model: Incomplete
    printer: Incomplete
    name: Incomplete
    reactor: Incomplete
    i2c: Incomplete
    report_time: Incomplete
    temp: float
    sample_timer: Incomplete
    is_calibrated: bool
    init_sent: bool
    def __init__(self, config) -> None: ...
    def handle_connect(self) -> None: ...
    min_temp: Incomplete
    max_temp: Incomplete
    def setup_minmax(self, min_temp, max_temp) -> None: ...
    def setup_callback(self, cb) -> None: ...
    def get_report_time_delta(self): ...
    def get_status(self, eventtime): ...

class AHT1x(AHTBase):
    model: str

class AHT2x(AHTBase):
    model: str

class AHT3x(AHTBase):
    model: str

def load_config(config) -> None: ...
