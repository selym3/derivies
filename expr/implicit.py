from .terms import const
from .expr import expr

class y(expr):

    def __init__(self, order=0):
        self.order = order  # how many times the derivative is taken

    def __str__(self):
        return '(y' + ("'" * self.order) + ')'

    def deriv(self):
        return y(self.order+1)

    def eval(self, xy):
        return const(xy[1])
