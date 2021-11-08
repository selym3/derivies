from .terms import const
from .exp import exp
from .ops import mul, pow


class cos(exp):
    def __init__(self, n: exp):
        self.n = n

    def __str__(self):
        return f'cos({self.n})'

    def deriv(self):
        return mul(mul(const(-1), sin(self.n)), self.n.deriv())


class sin(exp):

    def __init__(self, n: exp):
        self.n = n

    def __str__(self):
        return f'sin({self.n})'

    def deriv(self):
        return mul(cos(self.n), self.n.deriv())


class tan(exp):
    
    def __init__(self, n: exp):
        self.n = n

    def __str__(self):
        return f'tan({self.n})'

    def deriv(self):
        return mul(pow(sec(self.n), 2), self.n.deriv())

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
