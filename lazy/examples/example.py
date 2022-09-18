from datetime import date
from lazy import lazy


class C(object):

    @lazy
    def foo(self) -> str:
        return 'foo'

    @lazy
    def bar(self) -> str:
        return 'bar'

    @lazy
    def baz(self) -> int:
        return 42

    @lazy
    def quux(self) -> date:
        return date(2010, 10, 10)


class D(C):

    @lazy
    def foo(self) -> str:
        return super().foo


def f() -> None:
    c = C()
    'hello ' + c.foo
    'hello ' + c.bar
    1 + c.baz

    str(c.baz) == '42'
    c.quux.strftime('%y') == '10'

    lazy.invalidate(c, 'foo')

    type(C.foo) == lazy
    type(C.bar) == lazy

    type(c.foo) == str
    type(c.baz) == int

    d = D()
    'hello ' + d.foo
    'hello ' + super(D, d).foo


# Inherit from lazy
# Also see https://github.com/python/mypy/pull/8573/files
from typing import TYPE_CHECKING, TypeVar

_R = TypeVar('_R')


if TYPE_CHECKING:
    class cached(lazy[_R]): pass
else:
    class cached(lazy): pass


class E(object):
    @cached
    def foo(self) -> str:
        return 'foo'

    @cached
    def bar(self) -> str:
        return 'bar'

    @cached
    def baz(self) -> int:
        return 42

    @cached
    def quux(self) -> date:
        return date(2010, 10, 10)


def g() -> None:
    e = E()
    'hello' + e.foo
    'hello' + e.bar
    1 + e.baz

    str(e.baz) == '42'
    e.quux.strftime('%y') == '10'

    cached.invalidate(e, 'foo')


# Check Python >= 3.9
class Y(object):

    @lazy[str]
    def foo(self) -> str:
        return 'foo'

    @cached[str]
    def bar(self) -> str:
        return 'bar'

    @cached[int]
    def baz(self) -> int:
        return 42


def h() -> None:
    y = Y()
    'hello' + y.foo
    'hello' + y.bar
    1 + y.baz


# Check __class_getitem__ declaration
if TYPE_CHECKING:
    from typing import Any
    from types import GenericAlias

    class supercached(lazy[_R]):
        @classmethod
        def __class_getitem__(cls, params: Any) -> GenericAlias:
            return super().__class_getitem__(params)


if __name__ == '__main__':
    f()
    g()
    h()

