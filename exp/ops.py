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


class sub(exp):

    def __init__(self, l: exp, r: exp):
        self.l = l
        self.r = r

    def __str__(self):
        return f'({self.l} - {self.r})'

    def deriv(self):
        return sub(self.l.deriv(), self.r.deriv())


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


class div(exp):

    def __init__(self, n: exp, d: exp):
        self.n = n
        self.d = d

    def __str__(self):
        return f'{self.n} / {self.d}'

    def deriv(self):
        return div(
            sub(
                mul(self.d, self.n.deriv()),
                mul(self.n, self.d.deriv())
            ),
            pow(self.d, 2)
        )


class neg(exp):

    def __init__(self, e: exp):
        self.e = e 

    def __str__(self):
        return f'-{self.e}'

    def deriv(self):
        return neg(self.e.deriv())

class group(exp):

    def __init__(self, e: exp):
        self.e = e

    def __str__(self):
        return f'({self.e})'

    def deriv(self):
        return group(self.e.deriv())