from celery.bin.base import Command as Command
from typing import Any

class result(Command):
    args: str = ...
    def add_arguments(self, parser: Any) -> None: ...
    def run(self, task_id: Any, *args: Any, **kwargs: Any) -> None: ...