from enum import auto, Enum
from .expr import Expr, ExprInfo
from .parser import State

class BracketType(Enum):
    PAREN = auto()
    SQUARE = auto()
    CURLY = auto()

class LBracket(Expr):
    def __init__(self, id: str, btype: BracketType):
        super().__init__(id, ExprInfo(True, False, False))
        self.btype = btype

    def compute(self, _: State): pass
    def update(self, state: State): state.push_expr(self)


class RBracket(Expr):
    def __init__(self, id: str, btype: BracketType):
        super().__init__(id, ExprInfo(False, False, False))
        self.btype = btype

    def compute(self, state: State):
        # compute is only called when the state needs to 
        # update the number stack with an expression, but RHS
        # brackets should never be on the expression stack
        pass # no op

    def update(self, state: State):
        while (state.peek_expr() is not None) and (not state.peek_expr().is_lbracket()):
            state.pop_expr()
        
        # check for valid parenthesis
        if not state.has_expr(): raise Exception("missing closing bracket")
        if state.peek_expr().btype != self.btype: raise Exception("mismatched brackets")
        
        state.pop_expr() # this removes the left bracket
        while (state.peek_expr() is not None) and (state.peek_expr().is_function()):
            state.pop_expr() # consumes any functions that came before the left bracket