from . import probe as probe
from _typeshed import Incomplete

SIGNAL_PERIOD: float
MIN_CMD_TIME: Incomplete
TEST_TIME: Incomplete
RETRY_RESET_TIME: float
ENDSTOP_REST_TIME: float
ENDSTOP_SAMPLE_TIME: float
ENDSTOP_SAMPLE_COUNT: int
Commands: Incomplete

class BLTouchProbe:
    printer: Incomplete
    stow_on_each_sample: Incomplete
    probe_touch_mode: Incomplete
    mcu_pwm: Incomplete
    next_cmd_time: float
    finish_home_complete: Incomplete
    mcu_endstop: Incomplete
    output_mode: Incomplete
    next_test_time: float
    pin_up_not_triggered: Incomplete
    pin_up_touch_triggered: Incomplete
    pin_move_time: Incomplete
    get_mcu: Incomplete
    add_stepper: Incomplete
    get_steppers: Incomplete
    home_wait: Incomplete
    query_endstop: Incomplete
    homing_helper: Incomplete
    multi: str
    gcode: Incomplete
    def __init__(self, config, probe_offsets, param_helper) -> None: ...
    def start_probe_session(self, gcmd): ...
    wait_trigger_complete: Incomplete
    def home_start(self, print_time, sample_time, sample_count, rest_time, triggered: bool = True): ...
    def run_probe(self, gcmd) -> None: ...
    def pull_probed_results(self): ...
    def end_probe_session(self) -> None: ...
    cmd_BLTOUCH_DEBUG_help: str
    def cmd_BLTOUCH_DEBUG(self, gcmd) -> None: ...
    cmd_BLTOUCH_STORE_help: str
    def cmd_BLTOUCH_STORE(self, gcmd) -> None: ...

class PrinterBLTouch:
    printer: Incomplete
    probe_offsets: Incomplete
    param_helper: Incomplete
    mcu_probe: Incomplete
    probe_session: Incomplete
    cmd_helper: Incomplete
    def __init__(self, config) -> None: ...
    def get_probe_params(self, gcmd=None): ...
    def get_offsets(self, gcmd=None): ...
    def get_status(self, eventtime): ...
    def start_probe_session(self, gcmd): ...

def load_config(config): ...
