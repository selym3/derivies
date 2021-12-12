
import math

from parse import *

EXPRESSIONS = [
    # whitespace
    Skip(' '),
    Skip(','),
    Skip('\n'),

    # valid brackets
    LBracket('(', BracketType.PAREN),
    RBracket(')', BracketType.PAREN),
    LBracket('[', BracketType.SQUARE),
    RBracket(']', BracketType.SQUARE),
    LBracket('{', BracketType.CURLY),
    RBracket('}', BracketType.CURLY),
    
    # trig functions
    Function('sin', math.sin, 1),
    Function('cos', math.cos, 1),
    Function('tan', math.tan, 1),
    Function('csc', lambda x: 1 / math.sin(x), 1),
    Function('sec', lambda x: 1 / math.cos(x), 1),
    Function('cot', lambda x: 1 / math.tan(x), 1),

    # logic functions
    Function('max', max, params=Function.VARARGS), 
    Function('min', max, params=Function.VARARGS),

    Function('abs', abs, 1),

    # Constants
    Variable('pi', math.pi),
    Variable('e', math.e),

    # arithmetic
    Operator('^', lambda x, y: x**y, Assoc.RIGHT,4),
    Operator('/', lambda x, y: x/y, Assoc.LEFT,3),
    Operator('*', lambda x, y: x*y, Assoc.LEFT,3),
    Operator('+', lambda x, y: x+y, Assoc.LEFT,2),
    Operator('-', lambda x, y: x-y, Assoc.LEFT,2),
]

if __name__ == "__main__":
    import sys

    p = Parser(
        EXPRESSIONS,
        numeric_type=float
    )

    for line in sys.stdin:
        print(p.parse(line))