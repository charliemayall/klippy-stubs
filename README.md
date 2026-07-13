[![PyPI version](https://badge.fury.io/py/klippy-stubs.svg?icon=si%3Apython)](https://badge.fury.io/py/klippy-stubs)

# klippy-stubs

PEP 561 type stubs for [Klipper](https://www.klipper3d.org/)'s `klippy` package.

## Install

```bash
uv add klippy-stubs
# or
pip install klippy-stubs
```

Stubs install under `klippy/` (PEP 561).

Pyright, basedpyright, ty, and mypy
resolve `from klippy.*` imports with no extra configuration.

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

Verify the wheel

```bash
uv build
uv pip install dist/klippy_stubs-*.whl --force-reinstall
uv run ty check smoke_check.py
uv run mypy smoke_check.py
npx pyright smoke_check.py
```
