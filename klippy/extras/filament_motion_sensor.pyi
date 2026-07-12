from . import filament_switch_sensor as filament_switch_sensor
from _typeshed import Incomplete

CHECK_RUNOUT_TIMEOUT: float

class EncoderSensor:
    printer: Incomplete
    extruder_name: Incomplete
    detection_length: Incomplete
    reactor: Incomplete
    runout_helper: Incomplete
    get_status: Incomplete
    extruder: Incomplete
    estimated_print_time: Incomplete
    filament_runout_pos: Incomplete
    def __init__(self, config) -> None: ...
    def encoder_event(self, eventtime, state) -> None: ...

def load_config_prefix(config): ...
