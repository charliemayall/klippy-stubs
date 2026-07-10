from _typeshed import Incomplete

BATCH_INTERVAL: float

class BatchBulkHelper:
    printer: Incomplete
    batch_cb: Incomplete
    start_cb: Incomplete
    stop_cb: Incomplete
    is_started: bool
    batch_interval: Incomplete
    batch_timer: Incomplete
    client_cbs: Incomplete
    webhooks_start_resp: Incomplete
    def __init__(self, printer, batch_cb, start_cb=None, stop_cb=None, batch_interval=...) -> None: ...
    def add_client(self, client_cb) -> None: ...
    def add_mux_endpoint(self, path, key, value, webhooks_start_resp) -> None: ...

class BatchWebhooksClient:
    cconn: Incomplete
    template: Incomplete
    def __init__(self, web_request) -> None: ...
    def handle_batch(self, msg): ...

SENSOR_BULK_FMT: str

class BulkDataQueue:
    lock: Incomplete
    raw_samples: Incomplete
    def __init__(self, mcu, msg_fmt=..., oid=None) -> None: ...
    def pull_queue(self): ...
    def clear_queue(self) -> None: ...

class ClockSyncRegression:
    mcu: Incomplete
    chip_clock_smooth: Incomplete
    decay: Incomplete
    last_chip_clock: float
    mcu_clock_avg: float
    chip_clock_avg: float
    def __init__(self, mcu, chip_clock_smooth, decay=...) -> None: ...
    mcu_clock_variance: float
    def reset(self, mcu_clock, chip_clock) -> None: ...
    chip_clock_covariance: Incomplete
    def update(self, mcu_clock, chip_clock) -> None: ...
    last_exp_mcu_clock: Incomplete
    def set_last_chip_clock(self, chip_clock) -> None: ...
    def get_clock_translation(self): ...
    def get_time_translation(self): ...

MAX_BULK_MSG_SIZE: int

class FixedFreqReader:
    mcu: Incomplete
    clock_sync: Incomplete
    unpack_from: Incomplete
    bytes_per_sample: Incomplete
    samples_per_block: Incomplete
    last_sequence: int
    last_overflows: int
    bulk_queue: Incomplete
    def __init__(self, mcu, chip_clock_smooth, unpack_fmt) -> None: ...
    oid: Incomplete
    query_status_cmd: Incomplete
    def setup_query_command(self, msgformat, oid, cq) -> None: ...
    def get_last_overflows(self): ...
    def note_start(self) -> None: ...
    def note_end(self) -> None: ...
    def pull_samples(self): ...
