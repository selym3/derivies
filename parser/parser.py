from typing import List

class Node: pass

class Value(Node): 
    def __init__(self, value: float):
        self.value = value

    def __str__(self): return str(self.value)
    def __repr__(self): return f'Value({str(self)})'

class Add(Node):
    def __init__(self, l: Node, r: Node): self.l,self.r = l,r
    def __str__(self): return f'({self.l} + {self.r})'
    def __repr__(self): return f'Add{str(self)}'

# class Add(Node):
#     def __init__(self, l: Node, r: Node): self.l,self.r = l,r
#     def __str__(self): return f'({self.l} + {self.r})'
#     def __repr__(self): return f'Add{str(self)}'


class State:
    def __init__(self):
        self.numbers = []
        self.expressions = []

    def add_number(self, value: float):
        self.numbers.append(Value(value))

    def add_expr(self, expr):
        expr.update(self)

    def peek_expr(self): 
        return self.expressions[-1]

    def pop_expr(self):
        expr = self.expressions.pop()
        new_number = expr.compute(self)
        self.add_number(new_number)

    def pop_all(self):
        while len(self.expressions):
            self.pop_expr()
        return self.numbers[0]
class Expr:
    def __init__(self, id: str):
        self.id = id

    def is_lbracket(self):
        raise NotImplementedError

    def is_operator(self):
        raise NotImplementedError
    
    def compute(self, state):
        raise NotImplementedError

    def update(self, state: State):
        raise NotImplementedError


from enum import auto, Enum

class Assoc(Enum):
    LEFT = auto()
    RIGHT = auto()

class Operator(Expr):
    def __init__(self, id: str, assoc: Assoc, prec: int):
        super().__init__(id)
        self.assoc = assoc
        self.prec = prec

        # self.node = node


    def is_lbracket(self):
        return False

    def is_operator(self):
        return True

    def compute(self, state: State):
        r=state.numbers.pop()
        l=state.numbers.pop()

        return Add(l, r)

    def update(self, state: State):
        # expression at the top of the stack cannot be a left parenthesis,
        try: 
            expr = state.expressions[-1]
            while True:
                if expr.is_lbracket(): break
                if not expr.is_operator(): break
                
                if expr.prec>self.prec: 
                    state.pop_expr()
                elif expr.prec==self.prec and expr.assoc == Assoc.LEFT: 
                    state.pop_expr()
                else:
                    break
        except IndexError: pass
        state.expressions.append(self)


class Parser:
    def __init__(self, text: str, expressions: List[Expr]):
        # input
        self.text = text
        self.expressions = expressions

        # string parsing
        self.start = 0
        self.current = 0

        # output state
        self.state = State()

    def scan(self):
        while not self.empty():
            self.start = self.current
            if self.top().isdigit():
                self.scan_number()
            else:
                self.scan_expression()
        

    def scan_expression(self): 
        mexpr = None
        for expression in self.expressions:
            n = len(expression.id)
            if self.start+n<=len(self.text):
                snip = self.text[self.start:self.start+n]
                if snip == expression.id:
                    if (mexpr is None) or (len(snip) > len(mexpr.id)):
                        mexpr = expression

        if mexpr is None: 
            print("oopsy woopsy")
            self.current += 1
        else:
            self.state.add_expr(mexpr)
            self.current += len(mexpr.id)

    def scan_number(self):
        # add better number parsing
        while (not self.empty()) and (self.top().isdigit() or self.top() == '.'):
            self.current+=1
        self.state.add_number(float(self.text[self.start:self.current]))

    def empty(self):
        return self.current >= len(self.text)
        
    def top(self):
        return self.text[self.current]

p = Parser(
    "100/2/5", 
    [
        Operator('^',Assoc.RIGHT,4),
        Operator('/',Assoc.LEFT,3),
        Operator('*',Assoc.LEFT,3),
        Operator('+',Assoc.LEFT,2),
        Operator('-',Assoc.LEFT,2)
    ]
)

p.scan()
print(p.state.pop_all())