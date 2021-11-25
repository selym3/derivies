from tokens import Token

class Expr:
    pass

class Binary(Expr):
    def __init__(self, left: Expr, op: Token, right: Expr):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return f'({self.op.token_type} {self.left} {self.right})'

class Unary(Expr):
    def __init__(self, op:Token, right: Expr):
        self.right = right
        self.op = op

    def __str__(self):
        return f'({self.op.token_type} {self.right})'

class Literal(Expr):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'({self.value})'

class Grouping(Expr):
    def __init__(self, expr: Expr):
        self.expr = expr

    def __str__(self):
        return f'({self.expr})'

# class Binary(Expr):
#     def __init__(self, right: )