from typing import Any, Optional

class Events:
    receiver_cls: str = ...
    dispatcher_cls: str = ...
    state_cls: str = ...
    app: Any = ...
    def __init__(self, app: Optional[Any] = ...) -> None: ...
    def Receiver(self): ...
    def Dispatcher(self): ...
    def State(self): ...
    def default_dispatcher(self, hostname: Optional[Any] = ..., enabled: bool = ..., buffer_while_offline: bool = ...) -> None: ...