from enum import Enum, auto
from token import EQUAL

class TokenType(Enum):
    ''' defines the different types of lexemes for the scanner '''
    
    # grouping
    LPAREN = auto()
    RPAREN = auto()

    EQUAL

    # math operators
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    CAROT = auto()

    # math functions
    IDENTIFIER = auto()

    def __str__(self): return self._name_
    
class Token:
    ''' 
    fundamental unit for representing source text 
    
    the source text contains groups of characters to represent individual tokens, 
    so every other character can be removed and these groups of characters can
    be converted into individual tokens
    '''

    def __init__(self, token_type: TokenType, lexeme: str, literal: object = None):
        self.token_type = token_type
        self.lexeme = lexeme
        self.literal = literal
    
    def __str__(self):
        tkn = f'[ type={self.token_type} lexeme="{self.lexeme}" ' 
        if self.literal is not None:
            tkn += f'val={repr(self.literal)} '
        tkn += ']'
        return tkn

    def __repr__(self):
        return f'Token{str(self)}'

