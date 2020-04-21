from typing import Any, Optional

class Signal:
    receivers: Any = ...
    providing_args: Any = ...
    lock: Any = ...
    use_caching: Any = ...
    name: Any = ...
    sender_receivers_cache: Any = ...
    def __init__(self, providing_args: Optional[Any] = ..., use_caching: bool = ..., name: Optional[Any] = ...) -> None: ...
    def connect(self, *args: Any, **kwargs: Any): ...
    def disconnect(self, receiver: Optional[Any] = ..., sender: Optional[Any] = ..., weak: Optional[Any] = ..., dispatch_uid: Optional[Any] = ...): ...
    def has_listeners(self, sender: Optional[Any] = ...): ...
    def send(self, sender: Any, **named: Any): ...
    send_robust: Any = ...