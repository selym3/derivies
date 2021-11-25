from numbers import Number


class exp:
    def deriv(self):
        raise NotImplementedError

    def evalf(self, x: Number):
        raise NotImplementedError

    def evali(self, x: Number, y: Number):
        raise NotImplementedError