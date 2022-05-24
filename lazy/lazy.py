"""Decorator to create lazy attributes."""
from __future__ import annotations
from typing import TypeVar, Callable, Generic, overload, Union, Optional
import functools


T = TypeVar('T')
O = TypeVar('O')

class lazy(Generic[T, O]):
    """lazy descriptor

    Used as a decorator to create lazy attributes. Lazy attributes
    are evaluated on first use.
    """

    def __init__(self, func: Callable[[O], T]):
        self.__func = func
        functools.wraps(self.__func)(self)

    @overload
    def __get__(self, inst: None, inst_cls) -> lazy: ...

    @overload
    def __get__(self, inst: O, inst_cls) -> T: ...

    def __get__(self, inst: Optional[O], inst_cls) -> Union[lazy, T]:
        if inst is None:
            return self

        if not hasattr(inst, '__dict__'):
            raise AttributeError("'%s' object has no attribute '__dict__'" % (inst_cls.__name__,))

        name = self.__name__
        if name.startswith('__') and not name.endswith('__'):
            name = '_%s%s' % (inst_cls.__name__, name)

        value = self.__func(inst)
        inst.__dict__[name] = value
        return value

    @classmethod
    def invalidate(cls, inst, name):
        """Invalidate a lazy attribute.

        This obviously violates the lazy contract. A subclass of lazy
        may however have a contract where invalidation is appropriate.
        """
        inst_cls = inst.__class__

        if not hasattr(inst, '__dict__'):
            raise AttributeError("'%s' object has no attribute '__dict__'" % (inst_cls.__name__,))

        if name.startswith('__') and not name.endswith('__'):
            name = '_%s%s' % (inst_cls.__name__, name)

        if not isinstance(getattr(inst_cls, name), cls):
            raise AttributeError("'%s.%s' is not a %s attribute" % (inst_cls.__name__, name, cls.__name__))

        if name in inst.__dict__:
            del inst.__dict__[name]

