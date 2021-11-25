
from typing import List
from scan import Scanner
from tokens import Token, TokenType

from sys import stderr


from expr import *

class Parser:
    ''' utility class to turn a sequence of tokens into a syntax tree '''

    @staticmethod
    def parse(tokens):
        ''' utility method for interfacing with a parser '''
        if isinstance(tokens, str):
            tokens = Scanner.scan(tokens)

        parser = Parser(tokens)
        return parser.expression()

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        # self.
        self.current = 0

    #################
    # GRAMMAR RULES #
    #################

    def expression(self):
        return self.term()

    def term(self):
        left = self.factor()

        while self.match(TokenType.PLUS, TokenType.MINUS):
            operator = self.previous()
            right = self.factor()
            left = Binary(left, operator, right)

        return left
    
    def factor(self):
        left = self.unary()

        while self.match(TokenType.SLASH, TokenType.STAR):
            operator = self.previous()
            right = self.unary()
            left = Binary(left, operator, right)

        return left

    def unary(self):
        if self.match(TokenType.MINUS):
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)

        return self.exponent()

    def exponent(self):
        left = self.primary()

        while self.match(TokenType.CAROT):
            operator = self.previous()
            right = self.primary()
            left = Binary(left, operator, right)

        return left

    def primary(self):
        if self.match(TokenType.NUMBER):
            return Literal(self.previous().literal)

        if self.match(TokenType.IDENTIFIER):
            return None

        if self.match(TokenType.LPAREN):
            expr = self.expression()
            if not self.match(TokenType.RPAREN):
                print("no closing parenthesis for expression", file=stderr)
            return Grouping(expr)

        return None

    ###############
    # TOKEN LOGIC #
    ###############

    def match(self, *types: TokenType):
        for token_type in types:
            if self.check(token_type): 
                self.advance()
                return True
        return False

    def advance(self):
        if not self.is_empty(): self.current += 1
        return self.previous()
        
    def check(self, token_type: TokenType):
        if self.is_empty(): return False
        return self.peek().token_type == token_type

    def previous(self):
        return self.peek(offset=-1)

    def peek(self, offset=0):
        return self.tokens[self.current + offset]

    def is_empty(self):
        return self.current >= len(self.tokens)

if __name__ == "__main__":
    text = input()
    parsed = Parser.parse(text)
    print(parsed)