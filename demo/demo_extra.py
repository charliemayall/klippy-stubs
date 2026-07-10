"""Sample Klipper extra — type-checked with klippy-stubs, not runnable without Klipper."""

from __future__ import annotations

from klippy.configfile import ConfigWrapper
from klippy.gcode import GCodeCommand
from klippy.klippy import Printer
from klippy.toolhead import ToolHead


class DemoExtra:
    def __init__(self, config: ConfigWrapper) -> None:
        self.printer: Printer = config.get_printer()
        self.multiplier: float = config.getfloat("multiplier", 1.0, above=0.0)
        self.gcode = self.printer.lookup_object("gcode")
        self.gcode.register_command(
            "DEMO_BEEP", self.cmd_demo_beep, desc=self.cmd_DEMO_BEEP_help
        )
        self.gcode.register_command("DEMO_STATUS", self.cmd_demo_status)

    cmd_DEMO_BEEP_help = "Beep COUNT times (demo G-code param typing)"

    def cmd_demo_beep(self, gcmd: GCodeCommand) -> None:
        count: int = gcmd.get_int("COUNT", 1, minval=1, maxval=10)
        gcmd.respond_info(f"beep x{count} (multiplier={self.multiplier})", True)

    def cmd_demo_status(self, gcmd: GCodeCommand) -> None:
        toolhead: ToolHead = self.printer.lookup_object("toolhead")
        pos = toolhead.get_position()
        gcmd.respond_info(
            f"position x={pos[0]:.3f} y={pos[1]:.3f} z={pos[2]:.3f}", True
        )


def load_config(config: ConfigWrapper) -> DemoExtra:
    return DemoExtra(config)
