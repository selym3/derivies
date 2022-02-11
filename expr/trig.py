from .terms import const
from .expr import expr
from .ops import mul, pow


import math

class cos(expr):
    def __init__(self, n: expr):
        self.n = n

    def __str__(self):
        return f'cos({self.n})'

    def deriv(self):
        return mul(mul(const(-1), sin(self.n)), self.n.deriv())

    def eval(self, xy):
        return const(math.cos(self.n.eval(xy).value))

class sin(expr):

    def __init__(self, n: expr):
        self.n = n

    def __str__(self):
        return f'sin({self.n})'

    def deriv(self):
        return mul(cos(self.n), self.n.deriv())

    def eval(self, xy):
        return const(math.sin(self.n.eval(xy).value))

class tan(expr):
    
    def __init__(self, n: expr):
        self.n = n

    def __str__(self):
        return f'tan({self.n})'

    def deriv(self):
        return mul(pow(sec(self.n), const(2)), self.n.deriv())

    def eval(self, xy):
        return const(math.tan(self.n.eval(xy).value))

class sec(expr):
    
    def __init__(self, n: expr):
        self.n = n

    def __str__(self):
        return f'sec({self.n})'

    def deriv(self):
        return mul(
            mul(sec(self.n), tan(self.n)), 
            self.n.deriv()
        )

    def eval(self, xy):
        return const(1.0 / math.cos(self.n.eval(xy).value))

class csc(expr):
    
    def __init__(self, n: expr):
        self.n = n

    def __str__(self):
        return f'csc({self.n})'

    def deriv(self):
        return mul(
            mul(
                mul(
                    csc(self.n),
                    cot(self.n)
                ),
                const(-1)
            ),
            self.n.deriv()
        )

    def eval(self, xy):
        return const(1.0 / math.sin(self.n.eval(xy).value))

class cot(expr):

    def __init__(self, n: expr):
        self.n = n

    def __str__(self):
        return f'cot({self.n})'

    def deriv(self):
        return mul(
            mul(
                pow(csc(self.n), const(2)),
                const(-1)
            ),
            self.n.deriv()
        )

    def eval(self, xy):
        return const(1.0 / math.tan(self.n.eval(xy).value))
