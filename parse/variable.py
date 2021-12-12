from .expr import ExprInfo, Expr

class Variable(Expr):
    """
    a variable is a named value

    the parser reads a variables id and the variable 
    adds its given value directly to the number stack
     as if it were a number
    """
    
    def __init__(self, id: str, value):
        super().__init__(id, ExprInfo(False, False, False))
        self.value = value

    def compute(self, _): pass
    
    def update(self, state):
        state.add_num(self.value)