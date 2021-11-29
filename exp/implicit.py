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
        lvf = self.l.evalf(x).value
        rvf = self.r.evalf(x).value

        return const(1.0 if lvf==rvf else 0)

    def evali(self, x, y):
        lvi = self.l.evali(x, y).value
        rvi = self.r.evali(x, y).value

        return const(1.0 if lvi==rvi else 0)
