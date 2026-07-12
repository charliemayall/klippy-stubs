from . import bus as bus, tmc as tmc, tmc2130 as tmc2130
from _typeshed import Incomplete

Registers: Incomplete
ReadRegisters: Incomplete
Fields: Incomplete
SignedFields: Incomplete
FieldFormatters: Incomplete
MAX_CURRENT: float

class TMC2660CurrentHelper:
    printer: Incomplete
    name: Incomplete
    mcu_tmc: Incomplete
    fields: Incomplete
    current: Incomplete
    sense_resistor: Incomplete
    idle_current_percentage: Incomplete
    def __init__(self, config, mcu_tmc) -> None: ...
    def get_current(self): ...
    def set_current(self, run_current, hold_current, print_time) -> None: ...

class MCU_TMC2660_SPI:
    printer: Incomplete
    mutex: Incomplete
    spi: Incomplete
    name_to_reg: Incomplete
    fields: Incomplete
    def __init__(self, config, name_to_reg, fields) -> None: ...
    def get_fields(self): ...
    def get_register_raw(self, reg_name): ...
    def get_register(self, reg_name): ...
    def set_register(self, reg_name, val, print_time=None) -> None: ...
    def get_tmc_frequency(self) -> None: ...
    def get_mcu(self): ...

class TMC2660:
    fields: Incomplete
    mcu_tmc: Incomplete
    get_phase_offset: Incomplete
    get_status: Incomplete
    def __init__(self, config) -> None: ...

def load_config_prefix(config): ...
