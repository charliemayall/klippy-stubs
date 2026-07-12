from . import bus as bus
from _typeshed import Incomplete

REPORT_TIME: float
BME280_CHIP_ADDR: int
BME280_REGS: Incomplete
BMP388_REGS: Incomplete
BMP388_REG_VAL_PRESS_EN: int
BMP388_REG_VAL_TEMP_EN: int
BMP388_REG_VAL_PRESS_OS_NO: int
BMP388_REG_VAL_TEMP_OS_NO: int
BMP388_REG_VAL_ODR_50_HZ: int
BMP388_REG_VAL_DRDY_EN: int
BMP388_REG_VAL_NORMAL_MODE: int
BME680_REGS: Incomplete
BME680_GAS_CONSTANTS: Incomplete
BMP180_REGS: Incomplete
STATUS_MEASURING: Incomplete
STATUS_IM_UPDATE: int
MODE: int
MODE_PERIODIC: int
RUN_GAS: Incomplete
NB_CONV_0: int
EAS_NEW_DATA: Incomplete
GAS_IN_PROGRESS: Incomplete
MEASURE_IN_PROGRESS: Incomplete
RESET_CHIP_VALUE: int
BME_CHIPS: Incomplete
BME_CHIP_ID_REG: int
BMP3_CHIP_ID_REG: int

def get_twos_complement(val, bit_size): ...
def get_unsigned_short(bits): ...
def get_signed_short(bits): ...
def get_signed_byte(bits): ...
def get_unsigned_short_msb(bits): ...
def get_signed_short_msb(bits): ...

class BME280:
    printer: Incomplete
    name: Incomplete
    reactor: Incomplete
    i2c: Incomplete
    mcu: Incomplete
    iir_filter: Incomplete
    os_temp: Incomplete
    os_hum: Incomplete
    os_pres: Incomplete
    gas_heat_temp: Incomplete
    gas_heat_duration: Incomplete
    temp: float
    min_temp: float
    max_sample_time: Incomplete
    dig: Incomplete
    chip_type: str
    chip_registers: Incomplete
    last_gas_time: int
    def __init__(self, config) -> None: ...
    def handle_connect(self) -> None: ...
    max_temp: Incomplete
    def setup_minmax(self, min_temp, max_temp) -> None: ...
    def setup_callback(self, cb) -> None: ...
    def get_report_time_delta(self): ...
    def read_id(self): ...
    def read_bmp3_id(self): ...
    def read_register(self, reg_name, read_len): ...
    def write_register(self, reg_name, data) -> None: ...
    def get_status(self, eventtime): ...

def load_config(config) -> None: ...
