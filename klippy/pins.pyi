from _typeshed import Incomplete
from typing import TYPE_CHECKING, Any, Literal, NotRequired, TypedDict, overload

if TYPE_CHECKING:
    from klippy.mcu import MCU_adc, MCU_digital_out, MCU_endstop, MCU_pwm

class error(Exception): ...

re_pin: Incomplete

class PinParams(TypedDict):
    chip: Any
    chip_name: str
    pin: str
    invert: int
    pullup: int
    share_type: NotRequired[Any]

PinType = Literal["endstop", "digital_out", "pwm", "adc"]

class PinResolver:
    validate_aliases: bool
    reserved: dict[str, str]
    aliases: dict[str, str]
    active_pins: dict[str, str]
    def __init__(self, validate_aliases: bool = True) -> None: ...
    def reserve_pin(self, pin: str, reserve_name: str) -> None: ...
    def alias_pin(self, alias: str, pin: str) -> None: ...
    def update_command(self, cmd: str) -> str: ...

class PrinterPins:
    error = error
    chips: dict[str, Any]
    active_pins: dict[str, PinParams]
    pin_resolvers: dict[str, PinResolver]
    allow_multi_use_pins: dict[str, bool]
    def __init__(self) -> None: ...
    def parse_pin(
        self, pin_desc: str, can_invert: bool = False, can_pullup: bool = False
    ) -> PinParams: ...
    def lookup_pin(
        self,
        pin_desc: str,
        can_invert: bool = False,
        can_pullup: bool = False,
        share_type: Any = None,
    ) -> PinParams: ...
    # hand-refined: setup_pin discriminated by pin type
    @overload
    def setup_pin(self, pin_type: Literal["endstop"], pin_desc: str) -> MCU_endstop: ...
    @overload
    def setup_pin(
        self, pin_type: Literal["digital_out"], pin_desc: str
    ) -> MCU_digital_out: ...
    @overload
    def setup_pin(self, pin_type: Literal["pwm"], pin_desc: str) -> MCU_pwm: ...
    @overload
    def setup_pin(self, pin_type: Literal["adc"], pin_desc: str) -> MCU_adc: ...
    def reset_pin_sharing(self, pin_params: PinParams) -> None: ...
    def get_pin_resolver(self, chip_name: str) -> PinResolver: ...
    def register_chip(self, chip_name: str, chip: Any) -> None: ...
    def allow_multi_use_pin(self, pin_desc: str) -> None: ...

def add_printer_objects(config) -> None: ...
