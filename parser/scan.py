from tokens import Token, TokenType


def TokenAdder(token_type, literal=None):
    return lambda sc: sc.add_token(token_type, literal)

def DoNothing(sc): 
    return

class Scanner:
    ''' utility class for converting text into tokens '''

    @staticmethod
    def scan(text):
        ''' shorthand for using a scanner '''
        sc = Scanner(text)
        sc.scan_tokens()
        return sc.tokens

    def __init__(self, text):
        self.text = text
        self.start = 0
        self.current = 0

        self.tokens = []

    ################
    # LEXEME LOGIC #
    ################

    PATTERNS = {
        '=': TokenAdder(TokenType.EQUAL),
        
        '(': TokenAdder(TokenType.LPAREN),
        ')': TokenAdder(TokenType.RPAREN),

        '+': TokenAdder(TokenType.PLUS),
        '-': TokenAdder(TokenType.MINUS),
        '*': TokenAdder(TokenType.STAR),
        '/': TokenAdder(TokenType.SLASH),
        '^': TokenAdder(TokenType.CAROT),

        ' ' : DoNothing,
        '\r': DoNothing,
        '\t': DoNothing,
        '\n': DoNothing,
    }

    def scan_token(self):
        ''' logic implementing the scan of one token '''
        curr = self.advance()

        if curr in Scanner.PATTERNS:
            Scanner.PATTERNS[curr](self)
        elif curr.isdigit():
            self.add_number()
        elif curr.isalpha():
            self.add_identifier()
        else:
            raise ValueError("unknown start of token " + curr)

    def scan_tokens(self):
        ''' repeatedly scans tokens while there's still inputs '''
        while self.has_items():
            self.start = self.current
            self.scan_token()

    ###############
    # TOKEN LOGIC #
    ###############

    def add_token(self, token_type, literal=None, text=None):
        ''' helper for adding tokens to the scanners output '''
        text = text or self.text[self.start:self.current]
        self.tokens += [Token(token_type, text, literal)]

    def add_number(self):
        ''' token adder when needing to parse ints '''
        while self.peek().isdigit():
            self.advance()

        if self.peek() == '.' and self.peek_next().isdigit():
            self.advance()
            while self.has_items() and self.peek().isdigit(): self.advance() 

        numtxt = self.text[self.start:self.current]
        self.add_token(TokenType.NUMBER, literal=float(numtxt), text=numtxt)

    def add_identifier(self):
        while self.peek().isalnum():
            self.advance()

        self.add_token(TokenType.IDENTIFIER)

    ################
    # STRING LOGIC #
    ################

    def has_items(self):
        return self.current < len(self.text)

    def match(self, expected):
        ''' advances if the next character matches the expected one '''
        if not self.has_items(): return False
        if self.text[self.current] != expected: return False

        self.current += 1
        return True

    def advance(self):
        ''' advances past the current char after returning it '''
        curr = self.text[self.current]
        self.current += 1
        return curr

    def peek(self):
        if not self.has_items(): return '\x00'
        return self.text[self.current]

    def peek_next(self):
        if self.current + 1 >= len(self.text): return '\x00'
        return self.text[self.current + 1]


if __name__ == "__main__":
    s = Scanner.scan(input())
    print("\n".join((str(p) for p in s)))