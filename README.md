# klippy-stubs

PEP 561 type stubs for [Klipper](https://www.klipper3d.org/)'s `klippy` package.

## Install

```bash
uv add klippy-stubs
# or
pip install klippy-stubs
```

Type checkers pick up the stubs automatically after install.

```python
from klippy.configfile import ConfigWrapper
from klippy.klippy import Printer
from klippy.gcode import GCodeCommand
```

## Development

```bash
uv sync --dev
pre-commit install
uv run ty check smoke_check.py
```

To verify the installable package (required for mypy):

```bash
uv build
uv pip install dist/klippy_stubs-*.whl --force-reinstall
uv run mypy smoke_check.py
```
