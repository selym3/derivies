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

        self.param_stack = []

    def compute(self, _: State): 
        self.param_stack.pop()

    def update(self, state: State): 
        self.param_stack.append(state.num_count())
        state.push_expr(self)

    def param_count(self):
        if len(self.param_stack):
            return self.param_stack[-1]


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
        param_count = state.num_count() - state.peek_expr().param_count()
        
        # check for valid parenthesis
        if not state.has_expr(): raise Exception("missing closing bracket")
        if state.peek_expr().btype != self.btype: raise Exception("mismatched brackets")
        
        state.pop_expr() # this removes the left bracket
        while (state.peek_expr() is not None) and (state.peek_expr().is_function()):
            
            # if the function is varargs, tell it how many parameters to 
            # consume
            if state.peek_expr().varargs: 
                state.peek_expr().params = param_count
                # if there are functions next to each other (without a lbracket separating) 
                # then the outer functions (if varargs) only have 1 parameter (the inner function)
                param_count = 1 

            state.pop_expr() # consumes any functions that came before the left bracket