from numbers import Real
from .exp import exp


class const(exp):
    def __init__(self, value: Real):
        self.value = value

    def __str__(self):
        return str(self.value)

    def deriv(self):
        return const(0)


class x(exp):

    def __str__(self):
        return "x"

    def deriv(self):
        return const(1)
