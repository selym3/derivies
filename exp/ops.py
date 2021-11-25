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

    def evali(self, x, y):
        return const(
            self.l.evali(x, y).value +
            self.r.evali(x, y).value
        )

    def evalf(self, x):
        return const(
            self.l.evalf(x).value +
            self.r.evalf(x).value
        )

class sub(exp):

    def __init__(self, l: exp, r: exp):
        self.l = l
        self.r = r

    def __str__(self):
        return f'({self.l} - {self.r})'

    def deriv(self):
        return sub(self.l.deriv(), self.r.deriv())

    def evali(self, x, y):
        return const(
            self.l.evali(x, y).value - 
            self.r.evali(x, y).value
        )

    def evalf(self, x):
        return const(
            self.l.evalf(x).value - 
            self.r.evalf(x).value
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

    def evali(self, x, y):
        return const(
            self.l.evali(x, y).value *
            self.r.evali(x, y).value
        )

    def evalf(self, x):
        return const(
            self.l.evalf(x).value *
            self.r.evalf(x).value
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

    def evali(self, x, y):
        return const(
            self.a.evali(x, y).value **
            self.b.evali(x, y).value
        )

    def evalf(self, x):
        return const(
            self.a.evalf(x).value **
            self.b.evalf(x).value
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

    def evali(self, x, y):
        return const(
            self.n.evali(x, y).value /
            self.d.evali(x, y).value
        )

    def evalf(self, x):
        return const(
            self.n.evalf(x).value /
            self.d.evalf(x).value
        )


class neg(exp):

    def __init__(self, e: exp):
        self.e = e 

    def __str__(self):
        return f'-{self.e}'

    def deriv(self):
        return neg(self.e.deriv())

    def evali(self, x, y):
        return const(-self.e.evali(x, y).value)

    def evalf(self, x):
        return const(-self.e.evalf(x).value)

class group(exp):

    def __init__(self, e: exp):
        self.e = e

    def __str__(self):
        return f'({self.e})'

    def deriv(self):
        return group(self.e.deriv())

    def evali(self, x, y):
        return const(self.e.evali(x, y).value)

    def evalf(self, x):
        return const(self.e.evalf(x).value)