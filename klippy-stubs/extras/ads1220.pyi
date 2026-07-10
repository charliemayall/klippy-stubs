from . import bulk_sensor as bulk_sensor, bus as bus
from _typeshed import Incomplete

BYTES_PER_SAMPLE: int
MAX_SAMPLES_PER_MESSAGE: Incomplete
UPDATE_INTERVAL: float
RESET_CMD: int
START_SYNC_CMD: int
RREG_CMD: int
WREG_CMD: int
NOOP_CMD: int
RESET_STATE: Incomplete

def hexify(byte_array): ...

class ADS1220:
    printer: Incomplete
    name: Incomplete
    last_error_count: int
    consecutive_fails: int
    gain_options: Incomplete
    gain: Incomplete
    sps_normal: Incomplete
    sps_turbo: Incomplete
    sps_options: Incomplete
    sps: Incomplete
    is_turbo: Incomplete
    mux: Incomplete
    pga_bypass: Incomplete
    vref_options: Incomplete
    vref: Incomplete
    spi: Incomplete
    mcu: Incomplete
    oid: Incomplete
    data_ready_pin: Incomplete
    ffreader: Incomplete
    batch_bulk: Incomplete
    query_ads1220_cmd: Incomplete
    def __init__(self, config) -> None: ...
    def setup_trigger_analog(self, trigger_analog_oid) -> None: ...
    def get_mcu(self): ...
    def get_samples_per_second(self): ...
    def get_status(self, eventtime): ...
    def lookup_sensor_error(self, error_code): ...
    def get_range(self): ...
    def add_client(self, callback) -> None: ...
    def reset_chip(self) -> None: ...
    def setup_chip(self) -> None: ...
    def read_reg(self, reg, byte_count): ...
    def send_command(self, cmd) -> None: ...
    def write_reg(self, reg, register_bytes) -> None: ...

ADS1220_SENSOR_TYPE: Incomplete
