from _typeshed import Incomplete

BGFLUSH_LOW_TIME: float
BGFLUSH_HIGH_TIME: float
BGFLUSH_SG_LOW_TIME: float
BGFLUSH_SG_HIGH_TIME: float
BGFLUSH_EXTRA_TIME: float
MOVE_HISTORY_EXPIRE: float
MIN_KIN_TIME: float
STEPCOMPRESS_FLUSH_TIME: float
SDS_CHECK_TIME: float
DRIP_SEGMENT_TIME: float
DRIP_TIME: float

class PrinterMotionQueuing:
    printer: Incomplete
    reactor: Incomplete
    trapqs: Incomplete
    trapq_finalize_moves: Incomplete
    steppersyncmgr: Incomplete
    syncemitters: Incomplete
    syncemitter_to_name: Incomplete
    steppersyncs: Incomplete
    steppersyncmgr_gen_steps: Incomplete
    clear_history_time: float
    flush_callbacks: Incomplete
    kin_flush_delay: Incomplete
    all_mcus: Incomplete
    mcu: Incomplete
    can_pause: bool
    flush_timer: Incomplete
    do_kick_flush_timer: bool
    last_flush_time: float
    need_flush_time: float
    drip_start_times: Incomplete
    def __init__(self, config) -> None: ...
    def allocate_trapq(self): ...
    def wipe_trapq(self, trapq) -> None: ...
    def lookup_trapq_append(self): ...
    def allocate_syncemitter(self, mcu, name, alloc_stepcompress: bool = True): ...
    def setup_mcu_movequeue(self, mcu, serialqueue, move_count) -> None: ...
    def stats(self, eventtime): ...
    def register_flush_callback(
        self, callback, can_add_trapq: bool = False
    ) -> None: ...
    def unregister_flush_callback(self, callback) -> None: ...
    def get_kin_flush_delay(self): ...
    def check_step_generation_scan_windows(self) -> None: ...
    def flush_all_steps(self) -> None: ...
    def calc_step_gen_restart(self, est_print_time): ...
    need_step_gen_time: Incomplete
    def note_mcu_movequeue_activity(
        self, mq_time, is_step_gen: bool = True
    ) -> None: ...
    def drip_update_time(self, start_time, end_time, drip_completion) -> None: ...
    def check_drip_timing(self): ...

def load_config(config): ...
