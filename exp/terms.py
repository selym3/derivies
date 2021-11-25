from numbers import Number
from .exp import exp


class const(exp):
    def __init__(self, value: Number):
        self.value = value

    def __str__(self):
        return str(self.value)

    def deriv(self):
        return const(0)

    def evalf(self, x):
        return self
    
    def evali(self, x, y):
        return self


class x(exp):

    def __str__(self):
        return "x"

    def deriv(self):
        return const(1)

    def evalf(self, x):
        return const(x)

    def evali(self, x, y):
        return const(x)
