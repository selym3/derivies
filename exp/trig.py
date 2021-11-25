from .terms import const
from .exp import exp
from .ops import mul, pow


import math

class cos(exp):
    def __init__(self, n: exp):
        self.n = n

    def __str__(self):
        return f'cos({self.n})'

    def deriv(self):
        return mul(mul(const(-1), sin(self.n)), self.n.deriv())

    def evali(self, x, y):
        return const(math.cos(self.n.evali(x, y).value))

    def evalf(self, x):
        return const(math.cos(self.n.evalf(x).value))


class sin(exp):

    def __init__(self, n: exp):
        self.n = n

    def __str__(self):
        return f'sin({self.n})'

    def deriv(self):
        return mul(cos(self.n), self.n.deriv())

    def evali(self, x, y):
        return const(math.sin(self.n.evali(x, y).value))

    def evalf(self, x):
        return const(math.sin(self.n.evalf(x).value))

class tan(exp):
    
    def __init__(self, n: exp):
        self.n = n

    def __str__(self):
        return f'tan({self.n})'

    def deriv(self):
        return mul(pow(sec(self.n), 2), self.n.deriv())

    def evali(self, x, y):
        return const(math.tan(self.n.evali(x, y).value))

    def evalf(self, x):
        return const(math.tan(self.n.evalf(x).value))

class sec(exp):
    
    def __init__(self, n: exp):
        self.n = n

    def __str__(self):
        return f'sec({self.n})'

    def deriv(self):
        return mul(
            mul(sec(self.n), tan(self.n)), 
            self.n.deriv()
        )

    def evali(self, x, y):
        return const(1.0 / math.cos(self.n.evali(x, y).value))

    def evalf(self, x):
        return const(1.0 / math.cos(self.n.evalf(x).value))

class csc(exp):
    
    def __init__(self, n: exp):
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
                -1
            ),
            self.n.deriv()
        )

    def evali(self, x, y):
        return const(1.0 / math.sin(self.n.evali(x, y).value))

    def evalf(self, x):
        return const(1.0 / math.sin(self.n.evalf(x).value))

class cot(exp):

    def __init__(self, n: exp):
        self.n = n

    def __str__(self):
        return f'cot({self.n})'

    def deriv(self):
        return mul(
            mul(
                pow(csc(self.n), 2)
                -1,
            ),
            self.n.deriv()
        )

    def evali(self, x, y):
        return const(1.0 / math.tan(self.n.evali(x, y).value))

    def evalf(self, x):
        return const(1.0 / math.tan(self.n.evalf(x).value))


