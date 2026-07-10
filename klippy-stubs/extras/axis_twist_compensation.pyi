from . import bed_mesh as bed_mesh, manual_probe as manual_probe, probe as probe
from _typeshed import Incomplete

DEFAULT_SAMPLE_COUNT: int
DEFAULT_SPEED: float
DEFAULT_HORIZONTAL_MOVE_Z: float

class AxisTwistCompensation:
    printer: Incomplete
    gcode: Incomplete
    horizontal_move_z: Incomplete
    speed: Incomplete
    calibrate_start_x: Incomplete
    calibrate_end_x: Incomplete
    calibrate_y: Incomplete
    z_compensations: Incomplete
    compensation_start_x: Incomplete
    compensation_end_x: Incomplete
    calibrate_start_y: Incomplete
    calibrate_end_y: Incomplete
    calibrate_x: Incomplete
    compensation_start_y: Incomplete
    compensation_end_y: Incomplete
    zy_compensations: Incomplete
    calibrater: Incomplete
    def __init__(self, config) -> None: ...
    def clear_compensations(self, axis=None) -> None: ...

class Calibrater:
    compensation: Incomplete
    printer: Incomplete
    gcode: Incomplete
    probe: Incomplete
    lift_speed: Incomplete
    speed: Incomplete
    horizontal_move_z: Incomplete
    x_start_point: Incomplete
    x_end_point: Incomplete
    y_start_point: Incomplete
    y_end_point: Incomplete
    results: Incomplete
    current_point_index: Incomplete
    gcmd: Incomplete
    configname: Incomplete
    def __init__(self, compensation, config) -> None: ...
    cmd_AXIS_TWIST_COMPENSATION_CALIBRATE_help: str
    current_axis: Incomplete
    def cmd_AXIS_TWIST_COMPENSATION_CALIBRATE(self, gcmd) -> None: ...

def load_config(config): ...
