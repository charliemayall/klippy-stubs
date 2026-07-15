# Changelog

## 0.3.0

Hand-refined overloads beyond stubgen output:

- `Printer.lookup_object` - `Literal` names for `gcode`, `configfile`, `toolhead`, and `gcode_move`
- `ToolHead.manual_move` - `Sequence[float | None]` (`None` keeps the current axis)
- `ToolHead.set_max_velocities` - returns applied limits as a 4-tuple
- `LDC1612.add_client` - batch callback typed as `Callable[[dict[str, Any]], bool]`

`smoke_check.py` covers the new overloads.

## 0.2.0

Initial PyPI release: stubgen baseline plus refined overloads for `ConfigWrapper`, `GCodeCommand`, `setup_pin`, and `WebRequest`.
