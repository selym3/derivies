from .exp import exp
# from numbers import Real

from .terms import const

class add(exp):

    def __init__(self, l: exp, r: exp):
        self.l = l
        self.r = r

    def __str__(self):
        return f'({self.l} + {self.r})'

    def deriv(self):
        return add(self.l.deriv(), self.r.deriv())

    def eval(self, xy):
        return const(
            self.l.eval(xy).value +
            self.r.eval(xy).value
        )

class sub(exp):

    def __init__(self, l: exp, r: exp):
        self.l = l
        self.r = r

    def __str__(self):
        return f'({self.l} - {self.r})'

    def deriv(self):
        return sub(self.l.deriv(), self.r.deriv())

    def eval(self, xy):
        return const(
            self.l.eval(xy).value - 
            self.r.eval(xy).value
        )

class mul(exp):

    def __init__(self, l: exp, r: exp):
        self.l = l
        self.r = r

    def __str__(self):
        return f'({self.l} * {self.r})'

    def deriv(self):
        return add(
            mul(self.l, self.r.deriv()),
            mul(self.l.deriv(), self.r)
        )

    def eval(self, xy):
        return const(
            self.l.eval(xy).value *
            self.r.eval(xy).value
        )

class pow(exp):

    def __init__(self, a: exp, b: const):
        self.a = a
        self.b = b

    def __str__(self):
        return f'({self.a})^{self.b}'

    def deriv(self):
        return mul(
            mul(
                const(self.b),
                pow(self.a, const(self.b.value - 1))
            ),
            self.a.deriv()
        )

    def eval(self, xy):
        return const(
            self.a.eval(xy).value **
            self.b.eval(xy).value
        )

class div(exp):

    def __init__(self, n: exp, d: exp):
        self.n = n
        self.d = d

    def __str__(self):
        return f'({self.n} / {self.d})'

    def deriv(self):
        return div(
            sub(
                mul(self.d, self.n.deriv()),
                mul(self.n, self.d.deriv())
            ),
            pow(self.d, const(2))
        )

    def eval(self, xy):
        return const(
            self.n.eval(xy).value /
            self.d.eval(xy).value
        )
