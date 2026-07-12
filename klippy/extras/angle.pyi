from . import bulk_sensor as bulk_sensor, bus as bus
from _typeshed import Incomplete

MIN_MSG_TIME: float
TCODE_ERROR: int
TRINAMIC_DRIVERS: Incomplete
CALIBRATION_BITS: int
ANGLE_BITS: int

class AngleCalibration:
    printer: Incomplete
    name: Incomplete
    stepper_name: Incomplete
    tmc_module: Incomplete
    mcu_pos_offset: Incomplete
    angle_phase_offset: float
    calibration_reversed: bool
    calibration: Incomplete
    def __init__(self, config) -> None: ...
    def handle_sync_mcu_pos(self, mcu_stepper) -> None: ...
    def calc_mcu_pos_offset(self, sample) -> None: ...
    def apply_calibration(self, samples): ...
    def load_calibration(self, angles) -> None: ...
    def lookup_tmc(self): ...
    mcu_stepper: Incomplete
    def connect(self) -> None: ...
    def get_microsteps(self): ...
    def get_stepper_phase(self): ...
    def do_calibration_moves(self): ...
    def calc_angles(self, meas): ...
    cmd_ANGLE_CALIBRATE_help: str
    def cmd_ANGLE_CALIBRATE(self, gcmd) -> None: ...

class HelperA1333:
    SPI_MODE: int
    SPI_SPEED: int
    spi: Incomplete
    is_tcode_absolute: bool
    last_temperature: Incomplete
    def __init__(self, config, spi, oid) -> None: ...
    def get_static_delay(self): ...
    def start(self) -> None: ...

class HelperAS5047D:
    SPI_MODE: int
    SPI_SPEED: Incomplete
    spi: Incomplete
    is_tcode_absolute: bool
    last_temperature: Incomplete
    def __init__(self, config, spi, oid) -> None: ...
    def get_static_delay(self): ...
    def start(self) -> None: ...

class HelperTLE5012B:
    SPI_MODE: int
    SPI_SPEED: int
    printer: Incomplete
    spi: Incomplete
    oid: Incomplete
    is_tcode_absolute: bool
    last_temperature: Incomplete
    mcu: Incomplete
    spi_angle_transfer_cmd: Incomplete
    last_chip_mcu_clock: int
    chip_freq: float
    def __init__(self, config, spi, oid) -> None: ...
    def get_tcode_params(self): ...
    last_chip_clock: Incomplete
    def update_clock(self) -> None: ...
    def start(self) -> None: ...
    cmd_ANGLE_DEBUG_READ_help: str
    def cmd_ANGLE_DEBUG_READ(self, gcmd): ...
    cmd_ANGLE_DEBUG_WRITE_help: str
    def cmd_ANGLE_DEBUG_WRITE(self, gcmd): ...

class HelperMT6816:
    SPI_MODE: int
    SPI_SPEED: int
    printer: Incomplete
    spi: Incomplete
    oid: Incomplete
    mcu: Incomplete
    spi_angle_transfer_cmd: Incomplete
    is_tcode_absolute: bool
    last_temperature: Incomplete
    def __init__(self, config, spi, oid) -> None: ...
    def get_static_delay(self): ...
    def start(self) -> None: ...
    cmd_ANGLE_DEBUG_READ_help: str
    def cmd_ANGLE_DEBUG_READ(self, gcmd) -> None: ...

class HelperMT6826S:
    SPI_MODE: int
    SPI_SPEED: int
    printer: Incomplete
    stepper_name: Incomplete
    spi: Incomplete
    oid: Incomplete
    mcu: Incomplete
    spi_angle_transfer_cmd: Incomplete
    is_tcode_absolute: bool
    last_temperature: Incomplete
    status_map: Incomplete
    def __init__(self, config, spi, oid) -> None: ...
    def get_static_delay(self): ...
    def crc8(self, data): ...
    def start(self) -> None: ...
    def get_microsteps(self): ...
    cmd_ANGLE_CHIP_CALIBRATE_help: str
    def cmd_ANGLE_CHIP_CALIBRATE(self, gcmd) -> None: ...
    cmd_ANGLE_DEBUG_READ_help: str
    def cmd_ANGLE_DEBUG_READ(self, gcmd): ...

BYTES_PER_SAMPLE: int
SAMPLES_PER_BLOCK: Incomplete
SAMPLE_PERIOD: float
BATCH_UPDATES: float

class Angle:
    printer: Incomplete
    sample_period: Incomplete
    calibration: Incomplete
    start_clock: int
    last_sequence: int
    spi: Incomplete
    mcu: Incomplete
    oid: Incomplete
    sensor_helper: Incomplete
    query_spi_angle_cmd: Incomplete
    bulk_queue: Incomplete
    batch_bulk: Incomplete
    name: Incomplete
    def __init__(self, config) -> None: ...
    def get_status(self, eventtime=None): ...
    def add_client(self, client_cb) -> None: ...

def load_config_prefix(config): ...
