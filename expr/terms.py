from numbers import Number
from .expr import expr


class const(expr):
    def __init__(self, value: Number, name: str = None):
        self.value = value
        self.name = str(value) if name is None else name

    def __str__(self):
        return self.name

    def deriv(self):
        return const(0)

    def eval(self, _):
        return self
    
class x(expr):
    def __str__(self):
        return "x"

    def deriv(self):
        return const(1)

    def eval(self, xy):
        return const(xy[0])

