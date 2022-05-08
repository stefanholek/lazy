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


def f() -> None:
    c = C()
    'hello ' + c.foo
    'hello ' + c.bar
    # 'hello ' + c.baz

    lazy.invalidate(c, 'foo')

