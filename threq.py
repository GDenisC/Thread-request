
from threading import Thread
from typing import *
import requests
from enum import Enum

class MethodType(Enum):
    GET = requests.get
    POST = requests.post

__all__ = ('ThreadRequest', 'MethodType',)

def _CreateThread(target: Callable[..., object], *args, **kwargs) -> None:
    Thread(target=target, args=args, kwargs=kwargs).start()

def ThreadRequest(url: str, callback: Callable[[requests.Response], None], *, method: MethodType = MethodType.GET, args: Dict[str, Any] = {}, **kwargs: Dict[str, Any]) -> None:
    _CreateThread(target=lambda: callback(method(url, args, **kwargs)))
