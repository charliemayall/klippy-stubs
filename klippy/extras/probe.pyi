from . import manual_probe as manual_probe
from _typeshed import Incomplete
from typing import Any, Literal, NoReturn

from klippy import configfile
from klippy.gcode import GCodeCommand, GCodeDispatch
from klippy.mcu import MCU_endstop
from klippy.pins import PinParams
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from klippy.klippy import Printer

HINT_TIMEOUT: str

def calc_probe_z_average(
    positions: list[tuple[float, float, float]], method: str = "average"
) -> float: ...

class ProbeCommandHelper:
    printer: Printer
    probe: PrinterProbe
    query_endstop: Incomplete
    name: str
    last_state: bool
    last_probe_position: tuple[float, float, float] | None
    last_z_result: float
    probe_calibrate_info: Incomplete
    def __init__(
        self,
        config: configfile.ConfigWrapper,
        probe: PrinterProbe,
        query_endstop=None,
        can_set_z_offset: bool = True,
    ) -> None: ...
    def get_status(self, eventtime: float) -> dict[str, Any]: ...
    cmd_QUERY_PROBE_help: str
    def cmd_QUERY_PROBE(self, gcmd: GCodeCommand) -> None: ...
    cmd_PROBE_help: str
    def cmd_PROBE(self, gcmd: GCodeCommand) -> None: ...
    def probe_calibrate_finalize(self, mpresult) -> None: ...
    cmd_PROBE_CALIBRATE_help: str
    def cmd_PROBE_CALIBRATE(self, gcmd: GCodeCommand) -> None: ...
    cmd_PROBE_ACCURACY_help: str
    def cmd_PROBE_ACCURACY(self, gcmd: GCodeCommand) -> None: ...
    cmd_Z_OFFSET_APPLY_PROBE_help: str
    def cmd_Z_OFFSET_APPLY_PROBE(self, gcmd: GCodeCommand) -> None: ...

def lookup_minimum_z(config: configfile.ConfigWrapper) -> float: ...

class LookupZSteppers:
    printer: Printer
    add_stepper_cb: Incomplete
    def __init__(self, config: configfile.ConfigWrapper, add_stepper_cb) -> None: ...

class HomingViaProbeHelper:
    printer: Printer
    position_endstop: float
    query_endstop_cb: Incomplete
    def __init__(
        self,
        config: configfile.ConfigWrapper,
        position_endstop: float,
        query_endstop_cb=None,
    ) -> None: ...
    def get_mcu(self) -> NoReturn: ...
    def add_stepper(self, stepper) -> None: ...
    def get_steppers(self) -> list[Any]: ...
    def home_start(
        self,
        print_time: float,
        sample_time: float,
        sample_count: int,
        rest_time: float,
        triggered: bool = True,
    ) -> NoReturn: ...
    def home_wait(self, home_end_time: float) -> NoReturn: ...
    def query_endstop(self, print_time: float) -> bool: ...
    def get_position_endstop(self) -> float: ...
    def setup_pin(
        self, pin_type: Literal["endstop"], pin_params: PinParams
    ) -> HomingViaProbeHelper: ...

class DescendToEndstopHelper:
    printer: Printer
    mcu_probe: Incomplete
    probe_offsets: Incomplete
    param_helper: Incomplete
    always_check_movement: bool
    z_min_position: float
    results: list[tuple[float, float, float]]
    def __init__(
        self,
        config: configfile.ConfigWrapper,
        mcu_probe,
        probe_offsets,
        param_helper,
        always_check_movement: bool = False,
    ) -> None: ...
    def descend_until_trigger(self, gcmd: GCodeCommand) -> None: ...
    def pull_trigger_positions(self) -> list[tuple[float, float, float]]: ...
    def clear_trigger_positions(self) -> None: ...

class ProbeParameterHelper:
    dummy_gcode_cmd: GCodeCommand
    speed: float
    lift_speed: float
    sample_count: int
    sample_retract_dist: float
    samples_result: str
    samples_tolerance: float
    samples_retries: int
    def __init__(self, config: configfile.ConfigWrapper) -> None: ...
    def get_probe_params(self, gcmd: GCodeCommand | None = None) -> dict[str, Any]: ...

class SampleAveragingHelper:
    printer: Printer
    param_helper: ProbeParameterHelper
    start_session_cb: Incomplete
    hw_probe_session: Incomplete
    results: list[tuple[float, float, float]]
    def __init__(
        self,
        config: configfile.ConfigWrapper,
        param_helper: ProbeParameterHelper,
        start_session_cb,
    ) -> None: ...
    def start_probe_session(self, gcmd: GCodeCommand) -> Incomplete: ...
    def end_probe_session(self) -> None: ...
    def run_probe(self, gcmd: GCodeCommand) -> None: ...
    def pull_probed_results(self) -> list[tuple[float, float, float]]: ...

class ProbeOffsetsHelper:
    x_offset: float
    y_offset: float
    z_offset: float
    def __init__(self, config: configfile.ConfigWrapper) -> None: ...
    def get_offsets(
        self, gcmd: GCodeCommand | None = None
    ) -> tuple[float, float, float]: ...

class ProbePointsHelper:
    printer: Printer
    finalize_callback: Incomplete
    probe_points: list[tuple[float, float]]
    name: str
    gcode: GCodeDispatch
    default_horizontal_move_z: float
    speed: float
    use_offsets: bool
    lift_speed: float
    probe_offsets: ProbeOffsetsHelper
    manual_results: Incomplete
    def __init__(
        self,
        config: configfile.ConfigWrapper,
        finalize_callback,
        default_points: list[tuple[float, float]] | None = None,
    ) -> None: ...
    def minimum_points(self, n: int) -> None: ...
    def update_probe_points(
        self, points: list[tuple[float, float]], min_points: int
    ) -> None: ...
    def use_xy_offsets(self, use_offsets: bool) -> None: ...
    def get_lift_speed(self) -> float: ...
    horizontal_move_z: float
    def start_probe(self, gcmd: GCodeCommand) -> None: ...

def run_single_probe(
    probe: PrinterProbe, gcmd: GCodeCommand
) -> tuple[float, float, float]: ...

class ProbeEndstopWrapper:
    printer: Printer
    stow_on_each_sample: bool
    activate_gcode: str | None
    deactivate_gcode: str | None
    mcu_endstop: MCU_endstop
    query_endstop: Incomplete
    homing_helper: DescendToEndstopHelper
    multi: str
    def __init__(
        self,
        config: configfile.ConfigWrapper,
        probe_offsets: ProbeOffsetsHelper,
        param_helper: ProbeParameterHelper,
    ) -> None: ...
    def start_probe_session(self, gcmd: GCodeCommand) -> ProbeEndstopWrapper: ...
    def run_probe(self, gcmd: GCodeCommand) -> None: ...
    def pull_probed_results(self) -> list[tuple[float, float, float]]: ...
    def end_probe_session(self) -> None: ...

class PrinterProbe:
    printer: Printer
    probe_offsets: ProbeOffsetsHelper
    param_helper: ProbeParameterHelper
    mcu_probe: ProbeEndstopWrapper
    probe_session: Incomplete
    cmd_helper: ProbeCommandHelper
    def __init__(self, config: configfile.ConfigWrapper) -> None: ...
    def get_probe_params(self, gcmd: GCodeCommand | None = None) -> dict[str, Any]: ...
    def get_offsets(
        self, gcmd: GCodeCommand | None = None
    ) -> tuple[float, float, float]: ...
    def get_status(self, eventtime: float) -> dict[str, Any]: ...
    def start_probe_session(self, gcmd: GCodeCommand) -> ProbeEndstopWrapper: ...

def load_config(config: configfile.ConfigWrapper) -> PrinterProbe: ...
