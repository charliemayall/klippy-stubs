[![PyPI version](https://badge.fury.io/py/klippy-stubs.svg?icon=si%3Apython)](https://badge.fury.io/py/klippy-stubs)

# klippy-stubs

PEP 561 type stubs for [Klipper](https://www.klipper3d.org/)'s `klippy` package.

Most stubs come from mypy stubgen. Selected APIs get hand-refined overloads where stubgen loses precision (config getters, G-code param parsing, printer object lookup, pin setup, and similar).

## Install

```bash
uv add klippy-stubs
# or
pip install klippy-stubs
```

Stubs install under `klippy/` (PEP 561). Pyright, basedpyright, ty, and mypy resolve `from klippy.*` imports with no extra configuration.

```python
from klippy.configfile import ConfigWrapper
from klippy.klippy import Printer
from klippy.gcode import GCodeCommand

gcode = printer.lookup_object("gcode")  # typed as GCodeDispatch
toolhead = printer.lookup_object("toolhead")  # typed as ToolHead
```

## Hand-refined APIs

| Module                     | What stubgen misses                                                                      |
| -------------------------- | ---------------------------------------------------------------------------------------- |
| `configfile.ConfigWrapper` | Required vs optional getters (`get`, `getint`, `getfloat`, `getboolean`, lists, choices) |
| `gcode.GCodeCommand`       | Param parsers and sentinel defaults                                                      |
| `klippy.Printer`           | Named `lookup_object` targets (`gcode`, `configfile`, `toolhead`, `gcode_move`)          |
| `toolhead.ToolHead`        | `manual_move` partial coords (`None` = keep axis); `set_max_velocities` return tuple     |
| `extras.ldc1612.LDC1612`   | Bulk-sensor client callback signature                                                    |
| `pins` / `mcu`             | `setup_pin` discriminated by pin type                                                    |
| `webhooks.WebRequest`      | Typed request field getters                                                              |
| `msgproto`                 | MCU constant getters with sentinel default                                               |

See [CHANGELOG.md](CHANGELOG.md) for release notes.

Hand-refined sections are marked `# hand-refined:` in the `.pyi` files - grep before running stubgen.

## Development

```bash
uv sync --dev
pre-commit install
uv run ty check smoke_check.py
```

Verify the wheel:

```bash
uv build
uv pip install dist/klippy_stubs-*.whl --force-reinstall
uv run ty check smoke_check.py
uv run mypy smoke_check.py
npx pyright smoke_check.py
```

The `demo/` package is a minimal Klipper extra that exercises common stub paths.

### Pull Requests

PRs that simply re-run `mypy stubgen` and touch any `# hand-refined:` sections will be rejected. If a refinement looks wrong, open a PR with an example from the Klipper source code that demonstrates that shows the incorrect typing.

PRs that add new `# hand-refined:` sections are strongly encouraged. I don't have time, nor the understanding, to go through and hand-refine every API. Make a decent case for the refinement, as more hand-refined sections means more to maintain, so they need to add value.
