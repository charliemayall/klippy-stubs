from _typeshed import Incomplete
from typing import NamedTuple

shaper_defs: Incomplete
MIN_FREQ: float
MAX_FREQ: float
WINDOW_T_SEC: float
MAX_SHAPER_FREQ: float
TEST_DAMPING_RATIOS: Incomplete
AUTOTUNE_SHAPERS: Incomplete

class CalibrationData:
    name: Incomplete
    freq_bins: Incomplete
    psd_sum: Incomplete
    psd_x: Incomplete
    psd_y: Incomplete
    psd_z: Incomplete
    data_sets: Incomplete
    def __init__(self, name, freq_bins, psd_sum, psd_x, psd_y, psd_z) -> None: ...
    def add_data(self, other) -> None: ...
    numpy: Incomplete
    def set_numpy(self, numpy) -> None: ...
    def normalize_to_frequencies(self) -> None: ...
    def get_psd(self, axis: str = "all"): ...
    def get_datasets(self): ...

class CalibrationResult(NamedTuple):
    name: Incomplete
    freq: Incomplete
    freq_bins: Incomplete
    vals: Incomplete
    vibrs: Incomplete
    smoothing: Incomplete
    score: Incomplete
    max_accel: Incomplete

class ShaperCalibrate:
    printer: Incomplete
    error: Incomplete
    numpy: Incomplete
    def __init__(self, printer) -> None: ...
    def background_process_exec(self, method, args): ...
    def calc_freq_response(self, name, raw_values): ...
    def process_accelerometer_data(self, name, data): ...
    def fit_shaper(
        self,
        shaper_name,
        calibration_data,
        shaper_freqs,
        damping_ratio,
        scv,
        max_smoothing,
        max_vibrations,
        test_damping_ratios,
        max_freq,
    ): ...
    def find_shaper_max_accel(self, shaper, scv): ...
    def find_best_shaper(
        self,
        calibration_data,
        shapers=None,
        damping_ratio=None,
        scv=None,
        shaper_freqs=None,
        max_smoothing=None,
        max_vibrations=None,
        test_damping_ratios=None,
        max_freq=None,
        logger=None,
    ): ...
    def save_params(self, configfile, axis, shaper_name, shaper_freq) -> None: ...
    def apply_params(self, input_shaper, axis, shaper_name, shaper_freq) -> None: ...
    def save_calibration_data(
        self, output, calibration_data, shapers=None, max_freq=None
    ) -> None: ...
