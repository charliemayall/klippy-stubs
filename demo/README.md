# klippy-stubs demo

Minimal Klipper extra typed with [klippy-stubs](https://pypi.org/project/klippy-stubs/).

## Quick start

```bash
cd demo
uv sync --dev
uv run ty check demo_extra.py
uv run mypy demo_extra.py
```

## What it exercises

- `ConfigWrapper` getters (`getfloat` with `above=`)
- `GCodeCommand` param parsing (`get_int` with bounds)
- `config.get_printer()` → `Printer` via `from klippy.klippy import Printer`
- `Printer.lookup_object("toolhead")` → `ToolHead` (literal overload)
- `ToolHead.manual_move` with partial coords (`None` keeps axis)

See `sample.cfg` for the printer.cfg snippet.
