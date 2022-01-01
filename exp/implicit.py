from exp.terms import const
from .exp import exp

class y(exp):

    def __init__(self, order=0):
        self.order = order  # how many times the derivative is taken

    def __str__(self):
        return '(y' + ("'" * self.order) + ')'

    def deriv(self):
        return y(self.order+1)

    def evali(self, xy):
        return const(xy[1])

class eq(exp):
    
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return f'{self.l} = {self.r}'

    def deriv(self):
        return eq(self.l.deriv(), self.r.deriv())

    def eval(self, xy):
        x,y = xy

        lvf = self.l.eval(x).value
        rvf = self.r.eval(y).value

        return const(1.0 if lvf==rvf else 0)
