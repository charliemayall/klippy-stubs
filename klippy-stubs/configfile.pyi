import configparser
from _typeshed import Incomplete
from collections.abc import Callable, Mapping, Sequence
from typing import TYPE_CHECKING, Any, TypeVar, overload

if TYPE_CHECKING:
    from klippy.klippy import Printer

error = configparser.Error

class sentinel: ...

_T = TypeVar("_T")
_U = TypeVar("_U")
_V = TypeVar("_V")

class ConfigWrapper:
    error = configparser.Error
    printer: Printer
    fileconfig: Incomplete
    access_tracking: Incomplete
    section: str
    def __init__(self, printer, fileconfig, access_tracking, section) -> None: ...
    def get_printer(self) -> Printer: ...
    def get_name(self) -> str: ...
    @overload
    def get(
        self, option: str, default: type[sentinel] = ..., note_valid: bool = True
    ) -> str: ...
    @overload
    def get(self, option: str, default: _T, note_valid: bool = True) -> str | _T: ...
    @overload
    def getint(
        self,
        option: str,
        default: type[sentinel] = ...,
        minval: int | None = None,
        maxval: int | None = None,
        note_valid: bool = True,
    ) -> int: ...
    @overload
    def getint(
        self,
        option: str,
        default: _T,
        minval: int | None = None,
        maxval: int | None = None,
        note_valid: bool = True,
    ) -> int | _T: ...
    @overload
    def getfloat(
        self,
        option: str,
        default: type[sentinel] = ...,
        minval: float | None = None,
        maxval: float | None = None,
        above: float | None = None,
        below: float | None = None,
        note_valid: bool = True,
    ) -> float: ...
    @overload
    def getfloat(
        self,
        option: str,
        default: _T,
        minval: float | None = None,
        maxval: float | None = None,
        above: float | None = None,
        below: float | None = None,
        note_valid: bool = True,
    ) -> float | _T: ...
    @overload
    def getboolean(
        self, option: str, default: type[sentinel] = ..., note_valid: bool = True
    ) -> bool: ...
    @overload
    def getboolean(
        self, option: str, default: _T, note_valid: bool = True
    ) -> bool | _T: ...
    @overload
    def getchoice(
        self,
        option: str,
        choices: Mapping[_U, _V],
        default: type[sentinel] = ...,
        note_valid: bool = True,
    ) -> _V: ...
    @overload
    def getchoice(
        self,
        option: str,
        choices: Sequence[_U],
        default: type[sentinel] = ...,
        note_valid: bool = True,
    ) -> _U: ...
    @overload
    def getchoice(
        self,
        option: str,
        choices: Mapping[_U, _V],
        default: _T,
        note_valid: bool = True,
    ) -> _V | _T: ...
    @overload
    def getchoice(
        self, option: str, choices: Sequence[_U], default: _T, note_valid: bool = True
    ) -> _U | _T: ...
    @overload
    def getlists(
        self,
        option: str,
        default: type[sentinel] = ...,
        seps: tuple[str, ...] = (",",),
        count: int | None = None,
        parser: Callable[[str], _U] = ...,
        note_valid: bool = True,
    ) -> tuple[_U, ...]: ...
    @overload
    def getlists(
        self,
        option: str,
        default: _T,
        seps: tuple[str, ...] = (",",),
        count: int | None = None,
        parser: Callable[[str], _U] = ...,
        note_valid: bool = True,
    ) -> tuple[_U, ...] | _T: ...
    @overload
    def getlist(
        self,
        option: str,
        default: type[sentinel] = ...,
        sep: str = ",",
        count: int | None = None,
        note_valid: bool = True,
    ) -> tuple[str, ...]: ...
    @overload
    def getlist(
        self,
        option: str,
        default: _T,
        sep: str = ",",
        count: int | None = None,
        note_valid: bool = True,
    ) -> tuple[str, ...] | _T: ...
    @overload
    def getintlist(
        self,
        option: str,
        default: type[sentinel] = ...,
        sep: str = ",",
        count: int | None = None,
        note_valid: bool = True,
    ) -> tuple[int, ...]: ...
    @overload
    def getintlist(
        self,
        option: str,
        default: _T,
        sep: str = ",",
        count: int | None = None,
        note_valid: bool = True,
    ) -> tuple[int, ...] | _T: ...
    @overload
    def getfloatlist(
        self,
        option: str,
        default: type[sentinel] = ...,
        sep: str = ",",
        count: int | None = None,
        note_valid: bool = True,
    ) -> tuple[float, ...]: ...
    @overload
    def getfloatlist(
        self,
        option: str,
        default: _T,
        sep: str = ",",
        count: int | None = None,
        note_valid: bool = True,
    ) -> tuple[float, ...] | _T: ...
    def getsection(self, section: str) -> ConfigWrapper: ...
    def has_section(self, section: str) -> bool: ...
    def get_prefix_sections(self, prefix: str) -> list[ConfigWrapper]: ...
    def get_prefix_options(self, prefix: str) -> list[str]: ...
    def deprecate(self, option: str, value: Any = None) -> None: ...

class ConfigFileReader:
    def read_config_file(self, filename: str) -> Incomplete: ...
    def build_config_string(self, fileconfig) -> str: ...
    def append_fileconfig(self, fileconfig, data: str, filename: str) -> None: ...
    def build_fileconfig(self, data: str, filename: str) -> Incomplete: ...
    def build_fileconfig_with_includes(
        self, data: str, filename: str
    ) -> Incomplete: ...

AUTOSAVE_HEADER: str

class ConfigAutoSave:
    printer: Printer
    fileconfig: Incomplete
    status_save_pending: Incomplete
    save_config_pending: bool
    def __init__(self, printer) -> None: ...
    comment_r: Incomplete
    value_r: Incomplete
    def load_main_config(self) -> ConfigWrapper: ...
    def get_status(self, eventtime: float) -> dict[str, Any]: ...
    def set(self, section: str, option: str, value: str) -> None: ...
    def remove_section(self, section: str) -> None: ...
    cmd_SAVE_CONFIG_help: str
    def cmd_SAVE_CONFIG(self, gcmd) -> None: ...

class ConfigValidate:
    printer: Printer
    status_settings: Incomplete
    access_tracking: Incomplete
    autosave_options: Incomplete
    def __init__(self, printer) -> None: ...
    def start_access_tracking(self, autosave_fileconfig) -> None: ...
    def check_unused(self, fileconfig) -> None: ...
    def get_status(self, eventtime: float) -> dict[str, Any]: ...

class PrinterConfig:
    printer: Printer
    autosave: ConfigAutoSave
    validate: ConfigValidate
    deprecated: Incomplete
    status_raw_config: Incomplete
    status_warnings: Incomplete
    def __init__(self, printer) -> None: ...
    def get_printer(self) -> Printer: ...
    def read_config(self, filename: str) -> ConfigWrapper: ...
    def read_main_config(self) -> ConfigWrapper: ...
    def log_config(self, config: ConfigWrapper) -> None: ...
    def check_unused_options(self, config: ConfigWrapper) -> None: ...
    def runtime_warning(self, msg: str) -> None: ...
    def deprecate(
        self, section: str, option: str, value: Any = None, msg: str | None = None
    ) -> None: ...
    def deprecate_gcode(
        self,
        cmd: str,
        param: str | None = None,
        value: Any = None,
        msg: str | None = None,
    ) -> None: ...
    def deprecate_mcu_code(self, mcu, feature: str, msg: str | None = None) -> None: ...
    def get_status(self, eventtime: float) -> dict[str, Any]: ...
    def set(self, section: str, option: str, value: str) -> None: ...
    def remove_section(self, section: str) -> None: ...
