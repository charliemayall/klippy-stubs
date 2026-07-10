from . import output_pin as output_pin
from _typeshed import Incomplete

SERVO_SIGNAL_PERIOD: float
RESCHEDULE_SLACK: float

class PrinterServo:
    printer: Incomplete
    min_width: Incomplete
    max_width: Incomplete
    max_angle: Incomplete
    angle_to_width: Incomplete
    width_to_value: Incomplete
    last_value: float
    mcu_servo: Incomplete
    gcrq: Incomplete
    def __init__(self, config) -> None: ...
    def get_status(self, eventtime): ...
    cmd_SET_SERVO_help: str
    def cmd_SET_SERVO(self, gcmd) -> None: ...

def load_config_prefix(config): ...
