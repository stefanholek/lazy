import sys

from typing import TypeVar, Callable, Type, Generic
from typing import Optional, Any, overload

if sys.version_info >= (3, 9):
    from types import GenericAlias

_R = TypeVar("_R")


class lazy(Generic[_R]):
    __func: Callable[[Any], _R]

    def __init__(self, func: Callable[[Any], _R]) -> None: ...

    @overload
    def __get__(self, inst: None, inst_cls: Optional[Type[Any]] = ...) -> lazy[_R]: ...

    @overload
    def __get__(self, inst: object, inst_cls: Optional[Type[Any]] = ...) -> _R: ...

    @classmethod
    def invalidate(cls, inst: object, name: str) -> None: ...

    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, params: Any) -> GenericAlias: ...

