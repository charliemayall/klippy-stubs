from .display import display as display
from _typeshed import Incomplete

class GCodeRequestQueue:
    printer: Incomplete
    mcu: Incomplete
    callback: Incomplete
    rqueue: Incomplete
    next_min_flush_time: float
    toolhead: Incomplete
    motion_queuing: Incomplete
    def __init__(self, config, mcu, callback) -> None: ...
    def queue_gcode_request(self, value): ...
    def send_async_request(self, value, print_time=None) -> None: ...

RENDER_TIME: float

class PrinterTemplateEvaluator:
    printer: Incomplete
    active_templates: Incomplete
    render_timer: Incomplete
    templates: Incomplete
    create_template_context: Incomplete
    def __init__(self, config) -> None: ...
    def set_template(self, gcmd, callback, flush_callback=None) -> None: ...

def lookup_template_eval(config): ...

class PrinterOutputPin:
    printer: Incomplete
    is_pwm: Incomplete
    mcu_pin: Incomplete
    scale: Incomplete
    last_value: Incomplete
    shutdown_value: Incomplete
    gcrq: Incomplete
    template_eval: Incomplete
    def __init__(self, config) -> None: ...
    def get_status(self, eventtime): ...
    cmd_SET_PIN_help: str
    def cmd_SET_PIN(self, gcmd) -> None: ...

def load_config_prefix(config): ...
