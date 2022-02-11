
import math
from graph import graph_to_frame, Span, Region

from parse import *
import expr as e

from taylor import make_taylor_exp

def graph_preview(f: e.expr, a: e.const, b: e.const, c: e.const, d: e.const):
    preview_size = (40, 20)
    return graph_to_frame(f, Region(Span(a.value,c.value),Span(b.value,d.value)), preview_size)

# def curve_preview(x: e.exp, y: e.exp, )

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
    Variable('y', e.y()),
    Variable('pi', e.const(math.pi, 'pi')),
    Variable('tau', e.const(math.pi * 2, 'tau')),
    Variable('e', e.const(math.e, 'e')), # <-- probably want to replace this with an e.euler()

    # arithmetic
    Operator('^', e.pow, Assoc.RIGHT,4),
    Operator('/', e.div, Assoc.LEFT,3),
    Operator('*', e.mul, Assoc.LEFT,3),
    Operator('+', e.add, Assoc.LEFT,2),
    Operator('-', e.sub, Assoc.LEFT,2),

    # graphing
    Function('graph', graph_preview, params=5),
    Function('neg', lambda n: e.const(-n.value), params=1),
]

if __name__ == "__main__":
    import sys

    p = Parser(
        EXPRESSIONS,
        numeric_type=e.const
    )

    for line in sys.stdin:
        line = line.strip()
        print(p.parse(line))
