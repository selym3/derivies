from enum import auto, Enum
from .expr import Expr, ExprInfo

class Assoc(Enum):
    LEFT = auto()
    RIGHT = auto()

class Operator(Expr):
    def __init__(self, id: str, node, assoc: Assoc, prec: int):
        super().__init__(id, ExprInfo(False, True, False))
        self.assoc = assoc
        self.prec = prec

        self.node = node
    def compute(self, state):
        r=state.numbers.pop()
        l=state.numbers.pop()

        return self.node(l, r)

    def update(self, state):
        # expression at the top of the stack cannot be a left parenthesis,
        while expr := state.peek_expr():
            if expr.is_lbracket(): break
            if not expr.is_operator(): break
            
            if expr.prec>self.prec: 
                state.pop_expr()
            elif expr.prec==self.prec and expr.assoc == Assoc.LEFT: 
                state.pop_expr()
            else: 
                break

        state.push_expr(self)
