from . import adxl345 as adxl345, bulk_sensor as bulk_sensor, bus as bus
from _typeshed import Incomplete

REG_CHIPID: int
REG_ACC_DATA_START: int
REG_ACC_CONF: int
REG_ACC_RANGE: int
REG_FIFO_DOWNS: int
REG_FIFO_CONFIG_0: int
REG_FIFO_CONFIG_1: int
REG_FIFO_DATA: int
REG_FIFO_LENGTH_0: int
REG_CMD: int
REG_MOD_READ: int
CMD_ACC_PM_SUSPEND: int
CMD_ACC_PM_NORMAL: int
CMD_FIFO_FLUSH: int
BMI160_DEV_ID: int
SET_ACC_CONF_1600HZ: int
SET_ACC_RANGE_16G: int
SET_FIFO_CONFIG_1: int
SET_FIFO_DOWNS: int
FREEFALL_ACCEL: Incomplete
SCALE: Incomplete
BATCH_UPDATES: float
BMI_I2C_ADDR: int

class BMI160:
    printer: Incomplete
    reactor: Incomplete
    axes_map: Incomplete
    data_rate: int
    bus: Incomplete
    bus_type: str
    mcu: Incomplete
    oid: Incomplete
    query_bmi160_cmd: Incomplete
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
