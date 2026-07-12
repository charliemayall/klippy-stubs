from typing import Any

import cffi

FFI_main: cffi.FFI | None
FFI_lib: Any
pyhelper_logging_callback: Any

GCC_CMD: str
COMPILE_ARGS: str
SSE_FLAGS: str
SOURCE_FILES: list[str]
DEST_LIB: str
OTHER_FILES: list[str]
defs_stepcompress: str
defs_steppersync: str
defs_itersolve: str
defs_trapq: str
defs_kin_cartesian: str
defs_kin_generic_cartesian: str
defs_kin_corexy: str
defs_kin_corexz: str
defs_kin_delta: str
defs_kin_deltesian: str
defs_kin_polar: str
defs_kin_rotary_delta: str
defs_kin_winch: str
defs_kin_extruder: str
defs_kin_shaper: str
defs_kin_idex: str
defs_serialqueue: str
defs_trdispatch: str
defs_pyhelper: str
defs_std: str
defs_all: list[str]

def get_abs_files(srcdir: str, filelist: list[str]) -> list[str]: ...
def get_mtimes(filelist: list[str]) -> list[float]: ...
def check_build_code(sources: list[str], target: str) -> bool: ...
def check_gcc_option(option: str) -> bool: ...
def do_build_code(cmd: str) -> None: ...
def check_build_c_library() -> str: ...
def logging_callback(msg) -> None: ...
def get_ffi() -> tuple[cffi.FFI, Any]: ...

HC_COMPILE_CMD: str
HC_SOURCE_FILES: list[str]
HC_SOURCE_DIR: str
HC_TARGET: str
HC_CMD: str

def run_hub_ctrl(enable_power: bool) -> None: ...
