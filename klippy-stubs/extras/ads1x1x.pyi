from . import bus as bus
from _typeshed import Incomplete

ADS1X1X_CHIP_TYPE: Incomplete

def isADS101X(chip): ...
def isADS111X(chip): ...

ADS1X1X_CHIP_ADDR: Incomplete
ADS1X1X_REG_POINTER_MASK: int
ADS1X1X_REG_POINTER: Incomplete
ADS1X1X_REG_CONFIG: Incomplete
ADS1X1X_OS: Incomplete
ADS1X1X_MUX: Incomplete
ADS1X1X_PGA: Incomplete
ADS1X1X_PGA_VALUE: Incomplete
ADS111X_RESOLUTION: float
ADS111X_PGA_SCALAR: Incomplete
ADS101X_RESOLUTION: float
ADS101X_PGA_SCALAR: Incomplete
ADS1X1X_MODE: Incomplete
ADS101X_SAMPLES_PER_SECOND: Incomplete
ADS111X_SAMPLES_PER_SECOND: Incomplete
ADS1X1X_COMPARATOR_MODE: Incomplete
ADS1X1X_COMPARATOR_POLARITY: Incomplete
ADS1X1X_COMPARATOR_LATCHING: Incomplete
ADS1X1X_COMPARATOR_QUEUE: Incomplete
ADS1X1_OPERATIONS: Incomplete

class ADS1X1X_chip:
    name: Incomplete
    chip: Incomplete
    pga: Incomplete
    adc_voltage: Incomplete
    comp_mode: Incomplete
    comp_polarity: Incomplete
    comp_latching: Incomplete
    comp_queue: Incomplete
    mcu: Incomplete
    def __init__(self, config) -> None: ...
    def setup_pin(self, pin_type, pin_params): ...
    def is_ready(self): ...
    def calculate_sample_rate(self): ...
    delay: Incomplete
    def handle_report_time_update(self) -> None: ...
    def sample(self, pin): ...

class ADS1X1X_pin:
    mcu: Incomplete
    chip: Incomplete
    pcfg: Incomplete
    invalid_count: int
    def __init__(self, chip, pcfg) -> None: ...
    def check_invalid(self) -> None: ...
    def get_mcu(self): ...
    callback: Incomplete
    def setup_adc_callback(self, callback) -> None: ...
    report_time: Incomplete
    minval: Incomplete
    maxval: Incomplete
    range_check_count: Incomplete
    def setup_adc_sample(self, report_time, sample_time: float = 0.0, sample_count: int = 1, batch_num: int = 1, minval: float = 0.0, maxval: float = 1.0, range_check_count: int = 0) -> None: ...
    def get_last_value(self): ...

def load_config_prefix(config): ...
