from .terms import const
from .ops import div, mul
from .expr import expr
import math

class euler(const):
    def __init__(self): 
        super().__init__(math.e, 'e')

class log(expr):
    def __init__(self, n: expr, base: const = euler()):
        self.n = n
        self.base = base

    def __str__(self):
        return f'log{self.base}({self.n})'

    def deriv(self):
        # todo: add edge case for base of e?
        return div(self.n.deriv(), mul(log(self.base), self.n))

    def eval(self, xy):
        return const(math.log(self.n.eval(xy).value, base=self.base.eval(xy).value))
    
class pow(expr):
    def __init__(self, base: expr, exp: expr):
        self.base = base
        self.exp = exp

    def __str__(self):
        return f'({self.base})^({self.exp})'

    def deriv(self):
        baseconst = self.base is const
        expconst = self.exp is const

        if baseconst and expconst:
            # number^number and its derivative is 0
            return const(0.0)

        elif expconst:
            # function to the power of a number 
            
            # don't apply power rule to x^0 
            if self.exp.value == 0:
                return const(0.0)

            # apply power rule, d/dx(u^n) = (n * u^(n-1)) * d/dx(u)
            return mul(pow(self.base, const(self.exp.value - 1)), self.base.deriv())
        
        elif baseconst:
            # number to the power of a function
            return mul(self, log(self.exp))

        else:
            # function to the power of a function
            return mul(self, mul(log(self.base), self.exp).deriv())

# class exp(expr):
#     def __init__(self, n: expr):
#         self.n = n
#     def __str__(self):
#         return f'e^({self.n})'
#     def deriv(self):
#         return mul(self, self.n.deriv())
#     def eval(self, xy):
#         return const(math.exp(self.n.eval(xy).value))
