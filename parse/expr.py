class ExprInfo:
    """
    data about the type of expression

    there a few special types of expressions that
    have to be accounted for, like opening brackets,
    infix operators, and functions
    """
    def __init__(self, lbracket, operator, function):
        self.lbracket = lbracket
        self.operator = operator
        self.function = function

class Expr:
    """
    base class for an expression

    has functionality to add itself to the state's 
    expression stack and how to put itself on the
    number stack
    """
    def __init__(self, id: str, info: ExprInfo):
        self.id = id
        self.info = info

    def is_lbracket(self): return self.info.lbracket
    def is_operator(self): return self.info.operator
    def is_function(self): return self.info.function

    def compute(self, state): raise NotImplementedError
    def update(self, state): raise NotImplementedError

class Skip(Expr): 
    """ an expression that is skipped -- it's detected but ignored """

    # a skip sequence is valid but means nothing (e.g. whitespace)
    def __init__(self, id: str):
        super().__init__(id, ExprInfo(False, False, False))

    def compute(self, _): pass
    def update(self, _): pass