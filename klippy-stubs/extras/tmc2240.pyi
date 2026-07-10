from . import bus as bus, tmc as tmc, tmc2130 as tmc2130, tmc_uart as tmc_uart
from _typeshed import Incomplete

TMC_FREQUENCY: float
Registers: Incomplete
ReadRegisters: Incomplete
Fields: Incomplete
SignedFields: Incomplete
FieldFormatters: Incomplete

class TMC2240CurrentHelper:
    printer: Incomplete
    name: Incomplete
    mcu_tmc: Incomplete
    fields: Incomplete
    Rref: Incomplete
    req_hold_current: Incomplete
    def __init__(self, config, mcu_tmc) -> None: ...
    def get_current(self): ...
    def set_current(self, run_current, hold_current, print_time) -> None: ...

class TMC2240:
    fields: Incomplete
    mcu_tmc: Incomplete
    get_phase_offset: Incomplete
    get_status: Incomplete
    def __init__(self, config) -> None: ...

def load_config_prefix(config): ...
