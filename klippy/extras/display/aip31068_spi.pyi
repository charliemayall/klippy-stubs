from .. import bus as bus
from _typeshed import Incomplete

LINE_LENGTH_DEFAULT: int
LINE_LENGTH_OPTIONS: Incomplete
TextGlyphs: Incomplete

class CMND:
    CLR: int
    HOME: int
    ENTERY_MODE: Incomplete
    DISPLAY: Incomplete
    SHIFT: Incomplete
    FUNCTION: Incomplete
    CGRAM: Incomplete
    DDRAM: Incomplete
    WRITE_RAM: Incomplete

class flg_ENTERY_MODE:
    INC: Incomplete
    SHIFT: Incomplete

class flg_DISPLAY:
    ON: Incomplete
    CURSOR: Incomplete
    BLINK: Incomplete

class flg_SHIFT:
    WHOLE_DISPLAY: Incomplete
    RIGHT: Incomplete

class flg_FUNCTION:
    TWO_LINES: Incomplete
    FIVE_BY_ELEVEN: Incomplete

class flg_CGRAM:
    MASK: int

class flg_DDRAM:
    MASK: int

class flg_WRITE_RAM:
    MASK: int

DISPLAY_INIT_CMNDS: Incomplete

class aip31068_spi:
    printer: Incomplete
    spi: Incomplete
    mcu: Incomplete
    icons: Incomplete
    line_length: Incomplete
    text_framebuffers: Incomplete
    glyph_framebuffer: Incomplete
    all_framebuffers: Incomplete
    def __init__(self, config) -> None: ...
    @staticmethod
    def encode(data, width: int = 9): ...
    def send(self, data, minclock: int = 0) -> None: ...
    def flush(self) -> None: ...
    def init(self) -> None: ...
    def write_text(self, x, y, data) -> None: ...
    def set_glyphs(self, glyphs) -> None: ...
    def write_glyph(self, x, y, glyph_name): ...
    def write_graphics(self, x, y, data) -> None: ...
    def clear(self) -> None: ...
    def get_dimensions(self): ...
