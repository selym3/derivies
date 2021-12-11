from enum import auto, Enum
from .expr import Expr, ExprInfo

class Assoc(Enum):
    """ 
    associativity for an infix binary operator, 
    which can be left or right

    rules of associativity apply when there are 
    multiple operators of the same precedence in 
    a row without parenthesis. Are they executed left
    to right or right to left?

    Examples: 
     - 100/2/5 -> (100/2)/5 -> 50/5 -> 10
     - 4^3^2 -> 4^(3^2) -> 4^(9) -> 262144

    If the above examples are not calculated in the 
    shown order, they will yield different results.
    """ 

    LEFT = auto()
    RIGHT = auto()

class Operator(Expr):
    """
    an infix binary operator that takes into account 
    precedence (against other binary operators) and 
    left-right associativity. 

    the following rules apply when an operator is being 
    added to the parser's state:

     - the operator can be added to the stack if there is nothing
    else there or if the top is a left bracket or simply not another
    infix operator

        Take this expression:
        1 + 3 ^ 2
        
        After parsing:
        [1 3 2]
        [+ ^]

        Calculating the state is the same as converting to RPN:
        1 3 2 ^ + (<-- remember the rightmost operator is popped first)
        which is the same as (1 + (3^2)) which is what we started with


     - the operator cannot be added to the operator stack if 
    the top is an expression of higher precedence or it is the 
    same precedence but left associative

        Take this expression:
        1 ^ 3 + 2

        Trying to add +:
        [1 3]
        [^]

        If it is added without operator rules, the result will be:
        [1 3 2] [^ +], which is then
        1 3 2 + ^ --> 1^(3+2), which is incorrect

        With operator rules:
        (1 3 ^) 2 + --> (1^3) + 2 which is what we started with
    
    the operator class implements these rules in the update method,
    which is where an expression adds itself to the stack.

    the compute method pops takes two nodes from the number stack 
    and returns the binary node that the operator was created with
    (e.g. AddNode -- which takes in a left and right node) 
    """
    def __init__(self, id: str, node, assoc: Assoc, prec: int):
        super().__init__(id, ExprInfo(False, True, False))
        self.assoc = assoc
        self.prec = prec

        self.node = node
    def compute(self, state):
        r=state.pop_num()
        l=state.pop_num()

        return self.node(l, r)

    def update(self, state):
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
