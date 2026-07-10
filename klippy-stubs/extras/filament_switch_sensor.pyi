from _typeshed import Incomplete

class RunoutHelper:
    name: Incomplete
    printer: Incomplete
    reactor: Incomplete
    gcode: Incomplete
    runout_pause: Incomplete
    runout_gcode: Incomplete
    insert_gcode: Incomplete
    pause_delay: Incomplete
    event_delay: Incomplete
    min_event_systime: Incomplete
    filament_present: bool
    sensor_enabled: bool
    def __init__(self, config) -> None: ...
    def note_filament_present(self, eventtime, is_filament_present) -> None: ...
    def get_status(self, eventtime): ...
    cmd_QUERY_FILAMENT_SENSOR_help: str
    def cmd_QUERY_FILAMENT_SENSOR(self, gcmd) -> None: ...
    cmd_SET_FILAMENT_SENSOR_help: str
    def cmd_SET_FILAMENT_SENSOR(self, gcmd) -> None: ...

class SwitchSensor:
    runout_helper: Incomplete
    get_status: Incomplete
    def __init__(self, config) -> None: ...

def load_config_prefix(config): ...
