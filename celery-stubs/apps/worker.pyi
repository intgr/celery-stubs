from celery.worker import WorkController
from typing import Any, Optional

class Worker(WorkController):
    quiet: Any = ...
    def on_before_init(self, quiet: bool = ..., **kwargs: Any) -> None: ...
    redirect_stdouts: Any = ...
    redirect_stdouts_level: Any = ...
    purge: Any = ...
    no_color: Any = ...
    colored: Any = ...
    def on_after_init(self, purge: bool = ..., no_color: Optional[Any] = ..., redirect_stdouts: Optional[Any] = ..., redirect_stdouts_level: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def on_init_blueprint(self) -> None: ...
    def on_start(self) -> None: ...
    def emit_banner(self) -> None: ...
    def on_consumer_ready(self, consumer: Any) -> None: ...
    def setup_logging(self, colorize: Optional[Any] = ...): ...
    def purge_messages(self) -> None: ...
    def tasklist(self, include_builtins: bool = ..., sep: str = ..., int_: str = ...): ...
    def extra_info(self): ...
    def startup_info(self, artlines: bool = ...): ...
    def install_platform_tweaks(self, worker: Any) -> None: ...
    def macOS_proxy_detection_workaround(self) -> None: ...
    def set_process_status(self, info: Any): ...
