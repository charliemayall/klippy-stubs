from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any, TypeVar, overload

from reactor import ReactorMutex
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from klippy.klippy import Printer

class CommandError(Exception): ...

class Coord(tuple[float, float, float, float]):
    def __new__(cls, t: tuple[float, ...] | list[float]) -> Coord: ...
    @property
    def x(self) -> float: ...
    @property
    def y(self) -> float: ...
    @property
    def z(self) -> float: ...
    @property
    def e(self) -> float: ...

_T = TypeVar("_T")
_U = TypeVar("_U")

class GCodeCommand:
    error = CommandError
    respond_info: Callable[[str, bool], None]
    respond_raw: Callable[[str], None]
    def __init__(
        self,
        gcode,
        command: str,
        commandline: str,
        params: dict[str, str],
        need_ack: bool,
    ) -> None: ...
    def get_command(self) -> str: ...
    def get_commandline(self) -> str: ...
    def get_command_parameters(self) -> dict[str, str]: ...
    def get_raw_command_parameters(self) -> str: ...
    def ack(self, msg: str | None = None) -> None: ...

    class sentinel: ...

    @overload
    def get(
        self,
        name: str,
        default: type[sentinel] = ...,
        parser: Callable[[str], _U] = ...,
        minval: float | None = None,
        maxval: float | None = None,
        above: float | None = None,
        below: float | None = None,
    ) -> _U: ...
    @overload
    def get(
        self,
        name: str,
        default: _T,
        parser: Callable[[str], _U] = ...,
        minval: float | None = None,
        maxval: float | None = None,
        above: float | None = None,
        below: float | None = None,
    ) -> _U | _T: ...
    @overload
    def get_int(
        self,
        name: str,
        default: type[sentinel] = ...,
        minval: int | None = None,
        maxval: int | None = None,
    ) -> int: ...
    @overload
    def get_int(
        self,
        name: str,
        default: _T,
        minval: int | None = None,
        maxval: int | None = None,
    ) -> int | _T: ...
    @overload
    def get_float(
        self,
        name: str,
        default: type[sentinel] = ...,
        minval: float | None = None,
        maxval: float | None = None,
        above: float | None = None,
        below: float | None = None,
    ) -> float: ...
    @overload
    def get_float(
        self,
        name: str,
        default: _T,
        minval: float | None = None,
        maxval: float | None = None,
        above: float | None = None,
        below: float | None = None,
    ) -> float | _T: ...

class GCodeDispatch:
    error = CommandError
    Coord = Coord
    printer: Printer
    is_fileinput: bool
    is_printer_ready: bool
    mutex: ReactorMutex
    output_callbacks: list[Callable[[str], None]]
    base_gcode_handlers: dict[str, Callable[[GCodeCommand], None]]
    ready_gcode_handlers: dict[str, Callable[[GCodeCommand], None]]
    mux_commands: dict[str, dict[str, dict[str, Callable[[GCodeCommand], None]]]]
    gcode_help: dict[str, str]
    status_commands: dict[str, str]
    def __init__(self, printer) -> None: ...
    def is_traditional_gcode(self, cmd: str) -> bool: ...
    def register_command(
        self,
        cmd: str,
        func: Callable[[GCodeCommand], None],
        when_not_ready: bool = False,
        desc: str | None = None,
    ) -> None: ...
    def register_mux_command(
        self,
        cmd: str,
        key: str,
        value: str,
        func: Callable[[GCodeCommand], None],
        desc: str | None = None,
    ) -> None: ...
    def get_command_help(self) -> dict[str, str]: ...
    def get_status(self, eventtime: float) -> dict[str, Any]: ...
    def register_output_handler(self, cb: Callable[[str], None]) -> None: ...
    args_r: Incomplete
    def run_script_from_command(self, script: str) -> None: ...
    def run_script(self, script: str) -> None: ...
    def get_mutex(self) -> ReactorMutex: ...
    def create_gcode_command(
        self, command: str, commandline: str, params: dict[str, str]
    ) -> GCodeCommand: ...
    def respond_raw(self, msg: str) -> None: ...
    def respond_info(self, msg: str, log: bool = True) -> None: ...
    def cmd_default(self, gcmd: GCodeCommand) -> None: ...
    def cmd_M110(self, gcmd: GCodeCommand) -> None: ...
    def cmd_M112(self, gcmd: GCodeCommand) -> None: ...
    def cmd_M115(self, gcmd: GCodeCommand) -> None: ...
    def request_restart(self, result: str) -> None: ...
    cmd_RESTART_help: str
    def cmd_RESTART(self, gcmd: GCodeCommand) -> None: ...
    cmd_FIRMWARE_RESTART_help: str
    def cmd_FIRMWARE_RESTART(self, gcmd: GCodeCommand) -> None: ...
    def cmd_ECHO(self, gcmd: GCodeCommand) -> None: ...
    cmd_STATUS_help: str
    def cmd_STATUS(self, gcmd: GCodeCommand) -> None: ...
    cmd_HELP_help: str
    def cmd_HELP(self, gcmd: GCodeCommand) -> None: ...

class GCodeIO:
    printer: Printer
    gcode: GCodeDispatch
    gcode_mutex: ReactorMutex
    fd: int
    reactor: Incomplete
    is_printer_ready: bool
    is_processing_data: bool
    is_fileinput: bool
    pipe_is_active: bool
    fd_handle: Incomplete
    partial_input: str
    pending_commands: list[str]
    bytes_read: int
    input_log: Incomplete
    def __init__(self, printer) -> None: ...
    m112_r: Incomplete
    def stats(self, eventtime: float) -> tuple[bool, str]: ...

def add_early_printer_objects(printer) -> None: ...
