import lexer as lex
import errors as errors

class NumberNode ():
    def __init__(self, token):
        self.token = token

    def __str__(self):
        return f"{self.token}"

    
class OperationNode():
    def __init__ (self, left_node, operation_token, right_node):
        self.l_node = left_node
        self.op_token = operation_token
        self.r_node = right_node 

    def __str__(self):
        return f"({self.l_node}, {self.op_token}, {self.r_node})"

class Parser():

    def __init__(self, tokens): 
        self.tokens = tokens
        self.token_index = 0
        self.current_token = tokens[0]
        self.linenum =1
        self.fn = "future filename" 
    

    def parse(self):
        result = self.expression()
        return result

    def advance(self): 
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        else: 
            self.current_token = None
            
  
    def factor(self):   
        token = self.current_token
        if token.type in (lex.BC_INT, lex.BC_FLOAT):
            self.advance()
        return NumberNode(token)

    def term(self):
        left = self.factor()
        opTree = left
        while self.current_token is not None and self.current_token.type in (lex.BC_MULT, lex.BC_DIV):
            op_token = self.current_token
            self.advance() 
            right = self.factor()
            opTree = OperationNode(left, op_token, right)
        return opTree
    
    def expression(self):
        left = self.term()
        while self.current_token is not None and self.current_token.type in (lex.BC_PLUS, lex.BC_MINUS):
            op_token = self.current_token
            self.advance()
            right = self.term()
            left = OperationNode(left, op_token, right)
        return left