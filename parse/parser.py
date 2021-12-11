class State:
    """ 
    a state represents the progress of a parser working on a certain expression 
    
    a state contains two stacks -- one for numbers, another for expressions. 
    this will ultimately allow infix operations to calculated in the proper order,
    as operators can be added to a stack before being applied to valeuson the 
    number stack. 

    many state functions are just methods to interface with a stack. 
    """
    def __init__(self):
        self.nums = []
        self.exprs = []

    def add_num(self, value):
        self.nums.append(value)

    def add_expr(self, expr):
        """ 
        add an expression to the state (rather than just the stack).

        may require more expressions to be popped or for numbers to be
        used in some calculation.
        """
        expr.update(self)

    def push_expr(self, expr):
        self.exprs.append(expr)

    def peek_expr(self): 
        if len(self.exprs):
            return self.exprs[-1]

    def has_expr(self):
        return len(self.exprs)>0

    def has_num(self):
        return len(self.nums)>0

    def pop_expr(self):
        expr = self.exprs.pop()
        new_number = expr.compute(self)
        if new_number is not None:
            self.add_num(new_number)

    def pop_num(self):
        if self.has_num():
            return self.nums.pop()

    def pop_all(self):
        while len(self.exprs):
            self.pop_expr()
        return self.nums[0]

class Parser:
    """ 
    the parser is responsible for parsing a string input in infix form
    and producing some proper output.

    the parser will find number literals and expressions (+,-,*,etc) from
    their (sub)string couterparts and update the state with these tokens.

    the most important method in the parser is parse, which resets the internal
    state of the parser so it can work on a new input and it returns the result
    of its work (the parsed output).
    """

    def __init__(self, expressions, numeric_type=float):
        # lexemes
        self.expressions = expressions

        # type for numbers (leaf nodes) that expressions should expect
        # to work with
        self.numeric_type = numeric_type 


        # string parsing
        self.text = None
        self.start = 0
        self.current = 0

        # output state
        self.state = None # State()

    def reset(self, text):
        self.text = text
        self.state = State()
        self.start = 0
        self.current = 0

    def parse(self, text):
        """ get a parsed output from an infix text input """
        
        # reset internals 
        self.reset(text)
        
        # go through the input, 
        # looking for literals or expressions
        while not self.empty():
            self.start = self.current
            if self.top().isdigit():
                self.scan_number()
            else:
                self.scan_expression()

        # clear the state after all the input
        # has been exhausted
        return self.state.pop_all()
        

    def scan_expression(self): 
        """ 
        tries to match a substring to an expression 
        
        if a match is found, it is added to the state.
        if not, an error is thrown
        """
        mexpr = None
        for expression in self.expressions:
            n = len(expression.id)
            if self.start+n<=len(self.text):
                snip = self.text[self.start:self.start+n]
                if snip == expression.id:
                    if (mexpr is None) or (len(snip) > len(mexpr.id)):
                        mexpr = expression

        if mexpr is None: 
            raise Exception("unknown sequence")
        self.state.add_expr(mexpr)
        self.current += len(mexpr.id)

    def scan_number(self):
        """ 
        tries to match a substring with a floating point literal 
        and adds it to the state
        """

        # add better number parsing
        while (not self.empty()) and (self.top().isdigit() or self.top() == '.'):
            self.current+=1
        self.state.add_num(self.numeric_type(float(self.text[self.start:self.current])))

    def empty(self):
        return self.current >= len(self.text)
        
    def top(self):
        return self.text[self.current]