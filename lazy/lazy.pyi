from typing import TypeVar, Callable, Type, Generic
from typing import Optional, overload

_R = TypeVar("_R")
_C = TypeVar("_C")


class lazy(Generic[_R, _C]):

    def __init__(self, func: Callable[[_C], _R]) -> None: ...

    @overload
    def __get__(self, inst: None, inst_cls: Optional[Type[_C]] = ...) -> lazy[_R, _C]: ...

    @overload
    def __get__(self, inst: _C, inst_cls: Optional[Type[_C]] = ...) -> _R: ...

    @classmethod
    def invalidate(cls, inst: _C, name: str) -> None: ...

