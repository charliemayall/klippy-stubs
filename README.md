# klippy-stubs

PEP 561 type stubs for [Klipper](https://www.klipper3d.org/)'s `klippy` package.

## Install

```bash
uv add klippy-stubs
# or
pip install klippy-stubs
```

Type checkers pick up the stubs automatically after install.

## Development

```bash
uv sync --dev
uv run ty check
uv run python smoke_check.py
```

To verify the installable package (required for mypy):

```bash
uv build
uv pip install dist/klippy_stubs-*.whl --force-reinstall
uv run mypy smoke_check.py
```

## Layout

```
klippy-stubs/     # PEP 561 stub package (ships as site-packages/klippy-stubs/)
typings/          # dev-only stubs for klippy dependencies (cffi, greenlet)
smoke_check.py    # overload regression check (not shipped)
```
