from numbers import Number
from typing import List

class exp:
    def deriv(self):
        """ differentiate an expression """
        raise NotImplementedError

    def eval(self, xy=List[Number]):
        """ evaluate an expression """
        raise NotImplementedError
