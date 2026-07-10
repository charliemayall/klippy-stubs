from . import adxl345 as adxl345, bulk_sensor as bulk_sensor, bus as bus
from _typeshed import Incomplete

ICM20948_ADDR: int
ICM_DEV_IDS: Incomplete
REG_DEVID: int
REG_FIFO_EN: int
REG_ACCEL_SMPLRT_DIV1: int
REG_ACCEL_SMPLRT_DIV2: int
REG_ACCEL_CONFIG: int
REG_USER_CTRL: int
REG_PWR_MGMT_1: int
REG_PWR_MGMT_2: int
REG_INT_STATUS: int
REG_BANK_SEL: int
SAMPLE_RATE_DIVS: Incomplete
SET_BANK_0: int
SET_BANK_1: int
SET_BANK_2: int
SET_BANK_3: int
SET_ACCEL_CONFIG: int
SET_PWR_MGMT_1_WAKE: int
SET_PWR_MGMT_1_SLEEP: int
SET_PWR_MGMT_2_ACCEL_ON: int
SET_PWR_MGMT_2_OFF: int
SET_USER_FIFO_RESET: int
SET_USER_FIFO_EN: int
SET_ENABLE_FIFO: int
SET_DISABLE_FIFO: int
FREEFALL_ACCEL: Incomplete
SCALE: Incomplete
FIFO_SIZE: int
BATCH_UPDATES: float

class ICM20948:
    printer: Incomplete
    axes_map: Incomplete
    data_rate: Incomplete
    i2c: Incomplete
    mcu: Incomplete
    oid: Incomplete
    query_icm20948_cmd: Incomplete
    ffreader: Incomplete
    last_error_count: int
    batch_bulk: Incomplete
    name: Incomplete
    def __init__(self, config) -> None: ...
    def read_reg(self, reg): ...
    def set_reg(self, reg, val, minclock: int = 0) -> None: ...
    def start_internal_client(self): ...

def load_config(config): ...
def load_config_prefix(config): ...
