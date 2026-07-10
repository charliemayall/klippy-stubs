from . import filament_switch_sensor as filament_switch_sensor
from _typeshed import Incomplete

ADC_REPORT_TIME: float
ADC_SAMPLE_TIME: float
ADC_SAMPLE_COUNT: int

class HallFilamentWidthSensor:
    printer: Incomplete
    reactor: Incomplete
    pin1: Incomplete
    pin2: Incomplete
    dia1: Incomplete
    dia2: Incomplete
    rawdia1: Incomplete
    rawdia2: Incomplete
    MEASUREMENT_INTERVAL_MM: Incomplete
    nominal_filament_dia: Incomplete
    measurement_delay: Incomplete
    measurement_max_difference: Incomplete
    max_diameter: Incomplete
    min_diameter: Incomplete
    diameter: Incomplete
    is_active: Incomplete
    runout_dia_min: Incomplete
    runout_dia_max: Incomplete
    is_log: Incomplete
    enable_flow_compensation: Incomplete
    use_current_dia_while_delay: Incomplete
    sensor_disable_pending: bool
    flow_comp_disable_pending: bool
    array_clear_pending: bool
    filament_array: Incomplete
    lastFilamentWidthReading: int
    lastFilamentWidthReading2: int
    firstExtruderUpdatePosition: int
    filament_width: Incomplete
    toolhead: Incomplete
    ppins: Incomplete
    mcu_adc: Incomplete
    mcu_adc2: Incomplete
    extrude_factor_update_timer: Incomplete
    gcode: Incomplete
    runout_helper: Incomplete
    def __init__(self, config) -> None: ...
    def handle_ready(self) -> None: ...
    def adc_callback(self, samples) -> None: ...
    def adc2_callback(self, samples) -> None: ...
    def update_filament_array(self, last_epos) -> None: ...
    def extrude_factor_update_event(self, eventtime): ...
    cmd_QUERY_FILAMENT_WIDTH_help: str
    def cmd_M407(self, gcmd) -> None: ...
    cmd_RESET_FILAMENT_WIDTH_SENSOR_help: str
    def cmd_ClearFilamentArray(self, gcmd) -> None: ...
    cmd_ENABLE_FILAMENT_WIDTH_SENSOR_help: Incomplete
    def cmd_M405(self, gcmd) -> None: ...
    cmd_DISABLE_FILAMENT_WIDTH_SENSOR_help: str
    def cmd_M406(self, gcmd) -> None: ...
    cmd_QUERY_RAW_FILAMENT_WIDTH_help: str
    def cmd_Get_Raw_Values(self, gcmd) -> None: ...
    def get_status(self, eventtime): ...
    cmd_ENABLE_FILAMENT_WIDTH_LOG_help: str
    def cmd_log_enable(self, gcmd) -> None: ...
    cmd_DISABLE_FILAMENT_WIDTH_LOG_help: str
    def cmd_log_disable(self, gcmd) -> None: ...

def load_config(config): ...
