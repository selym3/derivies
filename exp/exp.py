from numbers import Number

class exp:
    def deriv(self):
        ''' any expression can return an expression that represents its derivative '''
        raise NotImplementedError

    def evalf(self, x: Number):
        ''' any expression can be evaluated and return a constant term '''
        raise NotImplementedError

    def evali(self, x: Number, y: Number):
        ''' eval function that supports implicit functions '''
        raise NotImplementedError