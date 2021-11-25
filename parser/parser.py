
from typing import List
from scan import Scanner
from tokens import Token, TokenType

# from expr import *

import sys
sys.path.append('../derivies') # add parent module??

import exp as e


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

            if operator.token_type == TokenType.PLUS:
                return e.add(left, right)
            else:
                return e.sub(left, right)
            # left = Binary(left, operator, right)

        return left
    
    def factor(self):
        left = self.unary()

        while self.match(TokenType.SLASH, TokenType.STAR):
            operator = self.previous()
            right = self.unary()

            if operator.token_type == TokenType.SLASH:
                return e.div(left, right)
            else:
                return e.mul(left, right)
            # left = Binary(left, operator, right)

        return left

    def unary(self):
        if self.match(TokenType.MINUS):
            operator = self.previous()
            right = self.unary()
            
            return e.neg(right)
            # return Unary(operator, right)

        return self.exponent()

    def exponent(self):
        left = self.primary()

        while self.match(TokenType.CAROT):
            operator = self.previous()
            right = self.primary()

            return e.pow(left, right)
            # left = Binary(left, operator, right)

        return left

    # def primary_number(self):
    #     if self.match(TokenType.NUMBER):

    def primary(self):
        if self.match(TokenType.NUMBER):
            return e.const(self.previous().literal) # Literal(self.previous().literal)

        if self.match(TokenType.IDENTIFIER):
            if self.previous().lexeme == 'x':
                return e.x()
            else:
                return e.y()
            
            # return None

        if self.match(TokenType.LPAREN):
            expr = self.expression()
            if not self.match(TokenType.RPAREN):
                print("no closing parenthesis for expression", file=stderr)
            return e.group(expr) # Grouping(expr)

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
    print(parsed.deriv())