
import math

from parse import *
import exp as e

from taylor import make_taylor_exp

EXPRESSIONS = [
    # whitespace
    Skip(' '),
    Skip(','),

    # valid brackets
    LBracket('(', BracketType.PAREN),
    RBracket(')', BracketType.PAREN),
    LBracket('[', BracketType.SQUARE),
    RBracket(']', BracketType.SQUARE),
    LBracket('{', BracketType.CURLY),
    RBracket('}', BracketType.CURLY),
    
    # trig functions
    Function('sin', e.sin, 1),
    Function('cos', e.cos, 1),
    Function('tan', e.tan, 1),
    Function('csc', e.csc, 1),
    Function('sec', e.sec, 1),
    Function('cot', e.cot, 1),

    # logic functions
    Function('max', lambda *args: max(*args, key=lambda c: c.value), params=Function.VARARGS), 
    Function('min', lambda *args: min(*args, key=lambda c: c.value), params=Function.VARARGS), 


    # differentiate
    Function('d', lambda n: n.deriv(), 1),
    Function('approx', lambda n: make_taylor_exp(n, 3), 1),
    
    # Constants
    Variable('x', e.x()),
    Variable('pi', math.pi),
    Variable('e', math.e), # <-- probably want to replace this with an e.euler()

    # arithmetic
    Operator('^', e.pow, Assoc.RIGHT,4),
    Operator('/', e.div, Assoc.LEFT,3),
    Operator('*', e.mul, Assoc.LEFT,3),
    Operator('+', e.add, Assoc.LEFT,2),
    Operator('-', e.sub, Assoc.LEFT,2),
]

if __name__ == "__main__":
    p = Parser(
        EXPRESSIONS,
        numeric_type=e.const
    )

    while True:
        print(p.parse(input()))

    # print(p.state.nums)
    # print(p.state.exprs)