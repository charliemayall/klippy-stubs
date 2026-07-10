from . import bulk_sensor as bulk_sensor, bus as bus
from _typeshed import Incomplete

NULL_CMD: int
RESET_CMD: int
STANDBY_CMD: int
WAKEUP_CMD: int
RESET_ACK: int
T_REGACQ: float
REG_ID: int
REG_STATUS: int
REG_MODE: int
REG_CLOCK: int
REG_GAIN1: int
REG_CFG: int
WORD24_MODE: int
PWR_MODE: int
GC_MODE: int
STATUS_REG_MASK: int
OSR_TO_REG: Incomplete
GAIN_TO_REG: Incomplete
GC_DLY_TO_REG: Incomplete
UPDATE_INTERVAL: float
MINIMUM_CLOCK_FREQ: int
MAXIMUM_CLOCK_FREQ: int
NOMINAL_CLOCK_FREQ: int
MAX_SAMPLE_RATE_DEVIATION: float

class ADS131M0X:
    printer: Incomplete
    name: Incomplete
    last_error_count: int
    consecutive_fails: int
    sensor_type: Incomplete
    sensor_id: Incomplete
    num_channels: Incomplete
    channel: Incomplete
    clock_freq: Incomplete
    gain: Incomplete
    enable_global_chop: Incomplete
    gc_dly: Incomplete
    osr: Incomplete
    sps: Incomplete
    spi: Incomplete
    mcu: Incomplete
    oid: Incomplete
    data_ready_pin: Incomplete
    ffreader: Incomplete
    batch_bulk: Incomplete
    query_ads131m0x_cmd: Incomplete
    def __init__(self, config, sensor_type, num_channels) -> None: ...
    def setup_trigger_analog(self, trigger_analog_oid) -> None: ...
    def get_mcu(self): ...
    def get_samples_per_second(self): ...
    def get_status(self, eventtime): ...
    def lookup_sensor_error(self, error_code): ...
    def get_range(self): ...
    def add_client(self, callback) -> None: ...
    def reset_chip(self) -> None: ...
    def setup_chip(self) -> None: ...
    def read_reg(self, reg): ...
    def write_reg(self, reg, value) -> None: ...
    def send_command_16(self, cmd, minclock: int = 0): ...

def ADS131M02(config): ...
def ADS131M04(config): ...

ADS131M0X_SENSOR_TYPES: Incomplete
