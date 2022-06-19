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
    # 'hello ' + c.baz
    1 + c.baz

    str(c.baz)
    c.quux.strftime('%y') == '10'

    lazy.invalidate(c, 'foo')

    type(C.foo) == lazy
    type(C.bar) == lazy

    type(c.foo) == str
    type(c.baz) == int

    d = D()
    'hello ' + d.foo
    'hello ' + super(D, d).foo

