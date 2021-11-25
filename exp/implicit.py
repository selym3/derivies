from exp.terms import const
from .exp import exp

class y(exp):

    def __init__(self, order=0):
        self.order = order  # how many times the derivative is taken

    def __str__(self):
        return '(y' + ("'" * self.order) + ')'

    def deriv(self):
        return y(self.order+1)

    def evali(self, x, y):
        return const(y)

class eq(exp):
    
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return f'{self.l} = {self.r}'

    def deriv(self):
        return eq(self.l.deriv(), self.r.deriv())

    def evalf(self, x):
        return eq(self.l.evalf(x), self.r.evalf(x))

    def evali(self, x, y):
        return eq(self.l.evali(x, y), self.r.evali(x, y))
