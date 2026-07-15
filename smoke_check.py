"""Smoke check for refined stub overloads. Run: uv run ty check smoke_check.py"""

from __future__ import annotations

from typing import cast

from klippy.configfile import ConfigWrapper, PrinterConfig
from klippy.extras.gcode_move import GCodeMove
from klippy.gcode import GCodeCommand, GCodeDispatch
from klippy.klippy import Printer
from klippy.mcu import MCU, MCU_endstop, MCU_pwm
from klippy.pins import PinParams, PrinterPins
from klippy.toolhead import ToolHead
from klippy.webhooks import WebRequest


def check_config(config: ConfigWrapper) -> None:
    printer: Printer = config.get_printer()
    assert printer is not None
    s: str = config.get("foo")
    i: int = config.getint("bar")
    f: float = config.getfloat("baz")
    b: bool = config.getboolean("qux")
    x: str | None = config.get("opt", None)
    assert isinstance(s, str)
    assert isinstance(i, int)
    assert isinstance(f, float)
    assert isinstance(b, bool)
    assert x is None or isinstance(x, str)


def check_gcode(gcmd: GCodeCommand) -> None:
    n: int = gcmd.get_int("S")
    v: float = gcmd.get_float("P")
    d: str | None = gcmd.get("X", None)
    assert isinstance(n, int)
    assert isinstance(v, float)
    assert d is None or isinstance(d, str)


def check_printer(printer: Printer) -> None:
    toolhead: ToolHead = printer.lookup_object("toolhead")
    gcode: GCodeDispatch = printer.lookup_object("gcode")
    configfile: PrinterConfig = printer.lookup_object("configfile")
    gcode_move: GCodeMove = printer.lookup_object("gcode_move")
    missing: object | None = printer.lookup_object("nope", None)
    reactor = printer.get_reactor()
    assert toolhead is not None
    assert gcode is not None
    assert configfile is not None
    assert gcode_move is not None
    assert missing is None or isinstance(missing, object)
    assert reactor is not None


def check_toolhead(toolhead: ToolHead) -> None:
    toolhead.manual_move([1.0, None, 0.0], 100.0)
    limits: tuple[float, float, float, float] = toolhead.set_max_velocities(
        100.0, 1000.0, 5.0, 0.5
    )
    assert len(limits) == 4


def check_setup_pin(pp: PrinterPins, m: MCU) -> None:
    endstop = pp.setup_pin("endstop", "^pe0")
    pwm = m.setup_pin(
        "pwm",
        cast(
            PinParams,
            {
                "chip": m,
                "chip_name": "mcu",
                "pin": "PE9",
                "invert": 0,
                "pullup": 0,
            },
        ),
    )
    assert isinstance(endstop, MCU_endstop)
    assert isinstance(pwm, MCU_pwm)


def check_webhooks(req: WebRequest) -> None:
    s: str = req.get_str("method")
    n: int | None = req.get_int("id", None)
    assert isinstance(s, str)
    assert n is None or isinstance(n, int)


if __name__ == "__main__":
    print("smoke_check: ty validates overloads; runtime asserts need real objects")
