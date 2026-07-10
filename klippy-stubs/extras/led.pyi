from . import output_pin as output_pin
from _typeshed import Incomplete

class LEDHelper:
    printer: Incomplete
    mutex: Incomplete
    update_func: Incomplete
    led_count: Incomplete
    need_transmit: bool
    led_state: Incomplete
    template_eval: Incomplete
    tcallbacks: Incomplete
    def __init__(self, config, update_func, led_count: int = 1) -> None: ...
    def get_status(self, eventtime=None): ...
    cmd_SET_LED_help: str
    def cmd_SET_LED(self, gcmd) -> None: ...
    cmd_SET_LED_TEMPLATE_help: str
    def cmd_SET_LED_TEMPLATE(self, gcmd) -> None: ...

class PrinterPWMLED:
    printer: Incomplete
    pins: Incomplete
    last_print_time: float
    led_helper: Incomplete
    prev_color: Incomplete
    def __init__(self, config) -> None: ...
    def update_leds(self, led_state, print_time) -> None: ...
    def get_status(self, eventtime=None): ...

def load_config_prefix(config): ...
