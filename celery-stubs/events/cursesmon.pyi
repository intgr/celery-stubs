import threading
from typing import Any, Optional

class CursesMonitor:
    keymap: Any = ...
    win: Any = ...
    screen_delay: int = ...
    selected_task: Any = ...
    selected_position: int = ...
    selected_str: str = ...
    foreground: Any = ...
    background: Any = ...
    online_str: str = ...
    help_title: str = ...
    help: str = ...
    greet: Any = ...
    info_str: str = ...
    app: Any = ...
    state: Any = ...
    lock: Any = ...
    def __init__(self, state: Any, app: Any, keymap: Optional[Any] = ...) -> None: ...
    def format_row(self, uuid: Any, task: Any, worker: Any, timestamp: Any, state: Any): ...
    @property
    def screen_width(self): ...
    @property
    def screen_height(self): ...
    @property
    def display_width(self): ...
    @property
    def display_height(self): ...
    @property
    def limit(self): ...
    def find_position(self): ...
    def move_selection_up(self) -> None: ...
    def move_selection_down(self) -> None: ...
    def move_selection(self, direction: int = ...) -> None: ...
    keyalias: Any = ...
    def handle_keypress(self) -> None: ...
    def alert(self, callback: Any, title: Optional[Any] = ...): ...
    def selection_rate_limit(self): ...
    def alert_remote_control_reply(self, reply: Any): ...
    def readline(self, x: Any, y: Any): ...
    def revoke_selection(self): ...
    def selection_info(self): ...
    def selection_traceback(self): ...
    def selection_result(self): ...
    def display_task_row(self, lineno: Any, task: Any) -> None: ...
    def draw(self) -> None: ...
    def safe_add_str(self, y: Any, x: Any, string: Any, *args: Any, **kwargs: Any) -> None: ...
    state_colors: Any = ...
    def init_screen(self) -> None: ...
    def resetscreen(self) -> None: ...
    def nap(self) -> None: ...
    @property
    def tasks(self): ...
    @property
    def workers(self): ...

class DisplayThread(threading.Thread):
    display: Any = ...
    shutdown: bool = ...
    def __init__(self, display: Any) -> None: ...
    def run(self) -> None: ...

def evtop(app: Optional[Any] = ...) -> None: ...
