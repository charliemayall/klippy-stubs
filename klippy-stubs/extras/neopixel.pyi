from . import led as led
from _typeshed import Incomplete

BACKGROUND_PRIORITY_CLOCK: int
BIT_MAX_TIME: float
RESET_MIN_TIME: float
MAX_MCU_SIZE: int

class PrinterNeoPixel:
    printer: Incomplete
    mcu: Incomplete
    oid: Incomplete
    pin: Incomplete
    neopixel_update_cmd: Incomplete
    color_map: Incomplete
    led_helper: Incomplete
    color_data: Incomplete
    old_color_data: Incomplete
    def __init__(self, config) -> None: ...
    neopixel_send_cmd: Incomplete
    def build_config(self) -> None: ...
    def update_color_data(self, led_state) -> None: ...
    def send_data(self, print_time=None) -> None: ...
    def update_leds(self, led_state, print_time) -> None: ...
    def get_status(self, eventtime=None): ...

def load_config_prefix(config): ...
