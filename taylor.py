import exp as e
from numbers import Number

poly_dict = dict[Number, int]

class poly:

    def __init__(self, terms: poly_dict = {}):
        self.order = -1
        self.terms = {}
        self.add_terms(terms)
        
    def is_valid(self):
        return len(self.terms) > 0
    
    def add_terms(self, terms: poly_dict):
        for exp, coeff in terms.items():
            self.add_term(coeff, exp)

    def add_term(self, coeff: Number, exp: int):
        # handle edge cases 
        if 0 > exp: raise ValueError(f"invalid exponent {exp}")
        if 0 == coeff: return 

        # if exponent in polynomial
        if exp in self.terms:
            # combine like terms
            self.terms[exp] += coeff

            # and if new coefficient is zero, delete that term
            if self.terms[exp] == 0:
                self.delete_term(exp)

        # otherwise, 
        else:
            # add new exponent to polynomial
            self.terms[exp] = coeff

            # and see if new term is leading term
            if exp > self.order:
                self.order = exp
        
    def delete_term(self, exp: int):
        if exp not in self.terms: return
        
        del self.terms[exp]
        if self.order == exp:
            self.order = self.find_order()

    def find_order(self):
        if not self.is_valid(): return -1
        return max((exp for exp in self.terms))

    def __str__(self):
        if not self.is_valid(): return 'DNE'

        vl = ''

        sorted_terms = list(self.terms.items())
        sorted_terms.sort(reverse=True)

        next_term = None
        for exp, coeff in sorted_terms:
            next_term = ' + ' if next_term else ''
            next_term += '' if coeff == 1 and exp > 0 else f'{coeff}'
            if exp > 0: next_term += 'x'
            if exp > 1: next_term += f'^{exp}'

            vl += next_term

        return vl

    def __repr__(self):
        return f'poly({self.terms})'


def make_taylor(exp: e.exp, upto: int) -> poly:
    p = poly()


    fact = 1
    for n in range(0, upto+1):
        p.add_term(
            coeff=exp.evalf(0).value/fact,
            exp=n
        )
        fact *= (n+1)
        exp = exp.deriv()
    
    return p

def make_taylor_exp(exp: e.exp, upto: int, approximate_at: e.const = e.const(0)) -> e.exp:
    p = None

    fact = 1
    for n in range(0, upto+1):
        term = e.mul(
            e.const(exp.evalf(0).value/fact),
            e.pow(
                e.sub(
                    e.x(),
                    approximate_at
                ),
                n
            ),
        )

        fact *= (n+1)
        p = term if p is None else e.add(p, term)
        exp = exp.deriv()
    
    return p

if __name__ == "__main__":
    f = e.cos(e.x())
    print(f)

    n = 4

    f_approx = make_taylor(f, n)
    print(f_approx)

    f_exp_approx = make_taylor_exp(f, n, e.const(1))
    print(f_exp_approx)

