from .expr import Expr, ExprInfo
from .parser import State

class Function(Expr):
    def __init__(self, id, func, params):
        super().__init__(id, ExprInfo(False, False, True))
        self.func = func
        self.params = params
    
    def compute(self, state: State):
        param_list = []
        while len(param_list) < self.params and state.has_num():
            param_list.append(state.pop_num())
        return self.func(*reversed(param_list))
    
    def update(self, state: State):
        state.push_expr(self)