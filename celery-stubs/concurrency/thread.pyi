from .base import BasePool
from typing import Any, Optional

class ApplyResult:
    f: Any = ...
    get: Any = ...
    def __init__(self, future: Any) -> None: ...
    def wait(self, timeout: Optional[Any] = ...) -> None: ...

class TaskPool(BasePool):
    body_can_be_buffer: bool = ...
    signal_safe: bool = ...
    limit: int = ...
    executor: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def on_stop(self) -> None: ...
    def on_apply(self, target: Any, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., callback: Optional[Any] = ..., accept_callback: Optional[Any] = ..., **_: Any): ...
