# flake8: noqa
# Stubs for sublime (Python 3.5)
from typing import Any, Callable, Dict, Optional, Sequence, Tuple, Union, List, Sized

DipType = float
LocationType = Tuple[str, str, Tuple[int, int]]
PointType = int

# Recursive type hinting is not supported so List and Dict are only defined
# properly up to one or two levels deep then set explicitly to accept Any.
ValueType = Union[
    Dict[
        Union[str, int],
        Union[
            bool, int, float, str,
            List[
                Union[
                    bool, int, float, str,
                    List[Any],
                    Dict[Union[str, int], Any]
                ]
            ],
            Dict[Union[str, int], Any]
        ]
    ],
    int, float, str, bool,
    List[
        Union[
            bool, int, float, str,
            List[Any],
            Dict[Union[str, int], Any]
        ]
    ]
]

DictValueType = Dict[str, ValueType]

VectorType = Tuple[DipType, DipType]


class _LogWriter:
    def flush(self) -> None: ...
    def write(self, s: str) -> None: ...

HOVER_TEXT = ...  # type: int
HOVER_GUTTER = ...  # type: int
HOVER_MARGIN = ...  # type: int
ENCODED_POSITION = ...  # type: int
TRANSIENT = ...  # type: int
FORCE_GROUP = ...  # type: int
IGNORECASE = ...  # type: int
LITERAL = ...  # type: int
MONOSPACE_FONT = ...  # type: int
KEEP_OPEN_ON_FOCUS_LOST = ...  # type: int
HTML = ...  # type: int
COOPERATE_WITH_AUTO_COMPLETE = ...  # type: int
HIDE_ON_MOUSE_MOVE = ...  # type: int
HIDE_ON_MOUSE_MOVE_AWAY = ...  # type: int
DRAW_EMPTY = ...  # type: int
HIDE_ON_MINIMAP = ...  # type: int
DRAW_EMPTY_AS_OVERWRITE = ...  # type: int
PERSISTENT = ...  # type: int
DRAW_OUTLINED = ...  # type: int
DRAW_NO_FILL = ...  # type: int
DRAW_NO_OUTLINE = ...  # type: int
DRAW_SOLID_UNDERLINE = ...  # type: int
DRAW_STIPPLED_UNDERLINE = ...  # type: int
DRAW_SQUIGGLY_UNDERLINE = ...  # type: int
HIDDEN = ...  # type: int
OP_EQUAL = ...  # type: int
OP_NOT_EQUAL = ...  # type: int
OP_REGEX_MATCH = ...  # type: int
OP_NOT_REGEX_MATCH = ...  # type: int
OP_REGEX_CONTAINS = ...  # type: int
OP_NOT_REGEX_CONTAINS = ...  # type: int
CLASS_WORD_START = ...  # type: int
CLASS_WORD_END = ...  # type: int
CLASS_PUNCTUATION_START = ...  # type: int
CLASS_PUNCTUATION_END = ...  # type: int
CLASS_SUB_WORD_START = ...  # type: int
CLASS_SUB_WORD_END = ...  # type: int
CLASS_LINE_START = ...  # type: int
CLASS_LINE_END = ...  # type: int
CLASS_EMPTY_LINE = ...  # type: int
INHIBIT_WORD_COMPLETIONS = ...  # type: int
INHIBIT_EXPLICIT_COMPLETIONS = ...  # type: int
DIALOG_CANCEL = ...  # type: int
DIALOG_YES = ...  # type: int
DIALOG_NO = ...  # type: int
UI_ELEMENT_SIDE_BAR = ...  # type: int
UI_ELEMENT_MINIMAP = ...  # type: int
UI_ELEMENT_TABS = ...  # type: int
UI_ELEMENT_STATUS_BAR = ...  # type: int
UI_ELEMENT_MENU = ...  # type: int
UI_ELEMENT_OPEN_FILES = ...  # type: int
LAYOUT_INLINE = ...  # type: int
LAYOUT_BELOW = ...  # type: int
LAYOUT_BLOCK = ...  # type: int

def version() -> str: ...
def platform() -> str: ...
def arch() -> str: ...
def channel() -> str: ...
def executable_path() -> str: ...
def executable_hash() -> str: ...
def packages_path() -> str: ...
def installed_packages_path() -> str: ...
def cache_path() -> str: ...
def status_message(msg: str) -> None: ...
def error_message(msg: str) -> None: ...
def message_dialog(msg: str) -> None: ...
def ok_cancel_dialog(msg: str, ok_title: str = ...) -> bool: ...
def yes_no_cancel_dialog(msg: str, yes_title: str = ..., no_title: str = ...) -> int: ...
def run_command(cmd: str, args: Dict[str, ValueType] = ...) -> None: ...
def get_clipboard(size_limit: int = ...) -> str: ...
def set_clipboard(text: str) -> None: ...
def log_commands(flag: bool) -> None: ...
def log_input(flag: bool) -> None: ...
def log_result_regex(flag: bool) -> None: ...
def log_indexing(flag: bool) -> None: ...
def log_build_systems(flag: bool) -> None: ...
def score_selector(scope_name: str, selector: str) -> int: ...
def load_resource(name: str) -> str: ...
def load_binary_resource(name: str) -> bytes: ...
def find_resources(pattern: str) -> Sequence[str]: ...
def encode_value(val: Any, pretty: bool = ...) -> str: ...
def decode_value(data: str) -> Any: ...
def expand_variables(val: Any, variables: DictValueType) -> Any: ...
def load_settings(base_name: str) -> Settings: ...
def save_settings(base_name: str) -> None: ...
def set_timeout(f: Callable[[], None], timeout_ms: int = ...) -> None: ...
def set_timeout_async(f: Callable[[], None], timeout_ms: int = ...) -> None: ...
def active_window() -> Window: ...
def windows() -> Sequence[Window]: ...
def get_macro() -> Sequence[DictValueType]: ...

class Window:
    window_id = ...  # type: int
    settings_object = ...  # type: Settings
    template_settings_object = ...  # type: Settings
    def __init__(self, id: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __bool__(self) -> bool: ...
    def id(self) -> int: ...
    def is_valid(self) -> bool: ...
    def hwnd(self) -> Any: ...
    def active_sheet(self) -> Sheet: ...
    def active_view(self) -> Optional[View]: ...
    def run_command(self, cmd: str, args: DictValueType = ...) -> None: ...
    def new_file(self, flags: int = ..., syntax: str = ...) -> View: ...
    def open_file(self, fname: str, flags: int = ..., group: int = ...) -> View: ...
    def find_open_file(self, fname: str) -> Optional[View]: ...
    def num_groups(self) -> int: ...
    def active_group(self) -> int: ...
    def focus_group(self, idx: int) -> None: ...
    def focus_sheet(self, sheet: Sheet) -> None: ...
    def focus_view(self, view: View) -> None: ...
    def get_sheet_index(self, sheet: Sheet) -> Tuple[int, int]: ...
    def get_view_index(self, view: View) -> Tuple[int, int]: ...
    def set_sheet_index(self, sheet: Sheet, group: int, idx: int) -> None: ...
    def set_view_index(self, view: View, group: int, idx: int) -> None: ...
    def sheets(self) -> List[Sheet]: ...
    def views(self) -> List[View]: ...
    def active_sheet_in_group(self, group: int) -> Optional[Sheet]: ...
    def active_view_in_group(self, group: int) -> Optional[View]: ...
    def sheets_in_group(self, group: int) -> List[Sheet]: ...
    def views_in_group(self, group: int) -> List[View]: ...
    def transient_sheet_in_group(self, group: int) -> Optional[Sheet]: ...
    def transient_view_in_group(self, group: int) -> Optional[View]: ...
    def layout(self) -> Dict[str, List[int]]: ...
    def get_layout(self) -> Dict[str, List[int]]: ...
    def set_layout(self, layout: Dict[str, List[int]]) -> None: ...
    def create_output_panel(self, name: str, unlisted: bool = ...) -> View: ...
    def find_output_panel(self, name: str) -> Optional[View]: ...
    def destroy_output_panel(self, name: str) -> None: ...
    def active_panel(self) -> Optional[str]: ...
    def panels(self) -> List[str]: ...
    def get_output_panel(self, name: str) -> View: ...
    def show_input_panel(self, caption: str, initial_text: str, on_done: Optional[Callable[[str], View]], on_change: Optional[Callable[[str], View]], on_cancel: Optional[Callable[[], View]]) -> View: ...
    def show_quick_panel(self, items: List[Any], on_select: Callable[[int], None], flags: int = ..., selected_index: int = ..., on_highlight: Callable[[str], None] = ...) -> None: ...
    def is_sidebar_visible(self) -> bool: ...
    def set_sidebar_visible(self, flag: bool) -> None: ...
    def is_minimap_visible(self) -> bool: ...
    def set_minimap_visible(self, flag: bool) -> None: ...
    def is_status_bar_visible(self) -> bool: ...
    def set_status_bar_visible(self, flag: bool) -> None: ...
    def get_tabs_visible(self) -> bool: ...
    def set_tabs_visible(self, flag: bool) -> None: ...
    def is_menu_visible(self) -> bool: ...
    def set_menu_visible(self, flag: bool) -> None: ...
    def folders(self) -> List[str]: ...
    def project_file_name(self) -> str: ...
    def project_data(self) -> Optional[DictValueType]: ...
    def set_project_data(self, v: DictValueType) -> None: ...
    def settings(self) -> Settings: ...
    def template_settings(self) -> Settings: ...
    def lookup_symbol_in_index(self, sym: str) -> List[str]: ...
    def lookup_symbol_in_open_files(self, sym: str) -> List[str]: ...
    def extract_variables(self) -> DictValueType: ...
    def status_message(self, msg: str) -> None: ...

class Edit:
    edit_token = ...  # type: int
    def __init__(self, token: int) -> None: ...

class Region:
    a = ...  # type: int
    b = ...  # type: int
    xpos = ...  # type: int
    def __init__(self, a: int, b: int = ..., xpos: int = ...) -> None: ...
    def __len__(self) -> int: ...
    def __eq__(self, rhs: object) -> bool: ...
    def __lt__(self, rhs: object) -> bool: ...
    def empty(self) -> bool: ...
    def begin(self) -> int: ...
    def end(self) -> int: ...
    def size(self) -> int: ...
    def contains(self, x: int) -> bool: ...
    def cover(self, rhs: Region) -> Region: ...
    def intersection(self, rhs: Region) -> Region: ...
    def intersects(self, rhs: Region) -> bool: ...

class Selection(Sized):
    view_id = ...  # type: int
    def __init__(self, id: int) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> Any: ...
    def __delitem__(self, index: int) -> None: ...
    def __eq__(self, rhs: object) -> bool: ...
    def __lt__(self, rhs: object) -> bool: ...
    def __bool__(self) -> bool: ...
    def is_valid(self) -> bool: ...
    def clear(self) -> None: ...
    def add(self, x: Region) -> None: ...
    def add_all(self, regions: Sequence[Region]) -> None: ...
    def subtract(self, region: Region) -> None: ...
    def contains(self, region: Region) -> bool: ...

class Sheet:
    sheet_id = ...  # type: Any
    def __init__(self, id: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def id(self) -> int: ...
    def window(self) -> Optional[Window]: ...
    def view(self) -> Optional[View]: ...

class View:
    view_id = ...  # type: int
    selection = ...  # type: Selection
    settings_object = ...  # type: Settings
    def __init__(self, id: int) -> None: ...
    def __len__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __bool__(self) -> bool: ...
    def id(self) -> int: ...
    def buffer_id(self) -> int: ...
    def is_valid(self) -> bool: ...
    def is_primary(self) -> bool: ...
    def window(self) -> Optional[Window]: ...
    def file_name(self) -> Optional[str]: ...
    def close(self) -> None: ...
    def retarget(self, new_fname: str) -> None: ...
    def name(self) -> str: ...
    def set_name(self, name: str) -> None: ...
    def is_loading(self) -> bool: ...
    def is_dirty(self) -> bool: ...
    def is_read_only(self) -> bool: ...
    def set_read_only(self, read_only: bool) -> None: ...
    def is_scratch(self) -> bool: ...
    def set_scratch(self, scratch: bool) -> None: ...
    def encoding(self) -> str: ...
    def set_encoding(self, encoding_name: str) -> None: ...
    def line_endings(self) -> str: ...
    def set_line_endings(self, line_ending_name: str) -> None: ...
    def size(self) -> int: ...
    def begin_edit(self, edit_token: int, cmd: str, args: DictValueType = ...) -> Edit: ...
    def end_edit(self, edit: Edit) -> None: ...
    def is_in_edit(self) -> bool: ...
    def insert(self, edit: Edit, pt: int, text: str) -> None: ...
    def erase(self, edit: Edit, r: Region) -> None: ...
    def replace(self, edit: Edit, r: Region, text: str) -> None: ...
    def change_count(self) -> int: ...
    def run_command(self, cmd: str, args: DictValueType = ...) -> None: ...
    def sel(self) -> Selection: ...
    def substr(self, x: Union[Region, int]) -> str: ...
    def find(self, pattern: str, start_pt: int, flags: Optional[int]) -> Region: ...
    def find_all(self, pattern: str, flags: Optional[int], fmt: Optional[Any], extractions: Optional[Any]) -> List[Region]: ...
    def settings(self) -> Settings: ...
    def meta_info(self, key: str, pt: int) -> Dict[str, Any]: ...
    def extract_scope(self, pt: int) -> Region: ...
    def scope_name(self, pt: int) -> str: ...
    def match_selector(self, pt: int, selector: str) -> bool: ...
    def score_selector(self, pt: int, selector: str) -> int: ...
    def find_by_selector(self, selector: str) -> List[Region]: ...
    def indented_region(self, pt: int) -> Region: ...
    def indentation_level(self, pt: int) -> int: ...
    def has_non_empty_selection_region(self) -> bool: ...
    def lines(self, r: Region) -> List[Region]: ...
    def split_by_newlines(self, r: Region) -> List[Region]: ...
    def line(self, x: Union[Region, int]) -> Region: ...
    def full_line(self, x: Union[Region, int]) -> Region: ...
    def word(self, x: Union[Region, int]) -> Region: ...
    def classify(self, pt: int) -> int: ...
    def find_by_class(self, pt: int, forward: bool, classes: int, separators: str = ...) -> int: ...
    def expand_by_class(self, x: Union[Region, int], classes: int, separators: str = ...) -> Region: ...
    def rowcol(self, tp: int) -> Tuple[int, int]: ...
    def text_point(self, row: int, col: int) -> int: ...
    def visible_region(self) -> Region: ...
    def show(self, x: Union[Selection, Region, int], show_surrounds: bool = ...) -> None: ...
    def show_at_center(self, x: Union[Selection, Region, int]) -> None: ...
    def viewport_position(self) -> Tuple[int, int]: ...
    def set_viewport_position(self, xy: Tuple[int, int], animate: bool = ...) -> None: ...
    def viewport_extent(self) -> Tuple[int, int]: ...
    def layout_extent(self) -> Tuple[int, int]: ...
    def text_to_layout(self, tp: int) -> Tuple[int, int]: ...
    def layout_to_text(self, xy: Tuple[int, int]) -> int: ...
    def window_to_layout(self, xy: Tuple[int, int]) -> Tuple[int, int]: ...
    def window_to_text(self, xy: Tuple[int, int]) -> int: ...
    def line_height(self) -> float: ...
    def em_width(self) -> float: ...
    def is_folded(self, sr: Region) -> bool: ...
    def folded_regions(self) -> List[Region]: ...
    def fold(self, x: Union[Region, List[Region]]) -> bool: ...
    def unfold(self, x: Union[Region, List[Region]]) -> List[Region]: ...
    def add_regions(self, key: str, regions: List[Region], scope: Optional[str], icon: Optional[str], flags: Optional[int]) -> None: ...
    def get_regions(self, key: str) -> List[Region]: ...
    def erase_regions(self, key: str) -> None: ...
    def add_phantom(self, key: str, region: Region, content: str, layout: int, on_navigate: Optional[Callable[[str], None]]) -> None: ...
    def erase_phantoms(self, key: str) -> None: ...
    def erase_phantom_by_id(self, pid: int) -> None: ...
    def query_phantom(self, pid: int) -> Phantom: ...
    def query_phantoms(self, pids: List[int]) -> List[Phantom]: ...
    def assign_syntax(self, syntax_file: str) -> None: ...
    def set_syntax_file(self, syntax_file: str) -> None: ...
    def symbols(self) -> List[Tuple[Region, str]]: ...
    def get_symbols(self) -> List[Tuple[Region, str]]: ...
    def indexed_symbols(self) -> List[Tuple[Region, str]]: ...
    def set_status(self, key: str, value: ValueType) -> None: ...
    def get_status(self, key: str) -> str: ...
    def erase_status(self, key: str) -> None: ...
    def extract_completions(self, prefix: str, tp: Optional[int]) -> List[str]: ...
    def find_all_results(self) -> List[Region]: ...
    def find_all_results_with_text(self) -> List[Region]: ...
    def command_history(self, delta: int, modifying_only: bool = ...) -> Tuple[str, DictValueType, int]: ...
    def overwrite_status(self) -> bool: ...
    def set_overwrite_status(self, value: bool) -> None: ...
    def show_popup_menu(self, items: List[str], on_select: Optional[Callable[[int], None]], flags: Optional[int]) -> None: ...
    def show_popup(self, content: str, flags: Optional[int], location: Optional[int], max_width: Optional[int], max_height: Optional[int], on_navigate: Optional[Callable[[str], None]], on_hide: Optional[Callable[[str], None]]) -> None: ...
    def update_popup(self, content: str) -> None: ...
    def is_popup_visible(self) -> bool: ...
    def hide_popup(self) -> None: ...
    def is_auto_complete_visible(self) -> bool: ...

class Settings:
    settings_id = ...  # type: int
    def __init__(self, id: int) -> None: ...
    def get(self, key: str, default: Optional[ValueType] = ...) -> ValueType: ...
    def has(self, key: str) -> bool: ...
    def set(self, key: str, value: ValueType) -> None: ...
    def erase(self, key: str) -> None: ...
    def add_on_change(self, tag: str, callback: Callable[[], None]) -> None: ...
    def clear_on_change(self, tag: str) -> None: ...

class Phantom:
    region = ...  # type: Region
    content = ...  # type: str
    layout = ...  # type: int
    on_navigate = ...  # type: Callable[[str], None]
    id = ...  # type: int
    def __init__(self, region: Region, content: str, layout: int, on_navigate: Optional[Callable[[str], None]]) -> None: ...
    def __eq__(self, rhs: object) -> bool: ...

class PhantomSet:
    view = ...  # type: View
    key = ...  # type: str
    phantoms = ...  # type: List[Phantom]
    def __init__(self, view: View, key: Optional[str]) -> None: ...
    def __del__(self) -> None: ...
    def update(self, new_phantoms: Sequence[Phantom]) -> None: ...
