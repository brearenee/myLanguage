import lexer as lex
import errors as errors

class NumberNode ():
    def __init__(self, token):
        self.token = token

    def __str__(self):
        return f"{self.token.type}: {self.token.value}"
    ##number node doesnt need a left/right because its a terminal/factor
    
##DONE
class OperationNode():
    def __init__ (self, left_node, operation_token, right_node):
            self.l_node = left_node
            self.op_token = operation_token
            self.r_node = right_node 
    def __str__(self):
        return f"({self.l_node}, {self.op_token}, {self.r_node})"

class Parser():
    ##Parser is taking in all of the tokens put in that list 
    # made from the Lexer.

    ##DONE
    def __init__(self, tokens): 
        self.tokens = tokens
        self.token_index = 0
        self.current_token = tokens[0]

    ##DONE
    def parse(self):
        result = self.expression()
        return result


    ##returns the next token from the list of tokens. 
    def advance(self): 
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
  
    ##checking if the current token is a terminal/factor. 
    def factor(self):   
        token = self.current_token
        if token.type in (lex.BC_INT, lex.BC_FLOAT):
            self.advance()
        return NumberNode(token)
        ##Do I need to return anything if its not a factor? 

    def term(self):
        left = self.factor()
        opTree = left
        while self.current_token in (lex.BC_MULT, lex.BC_DIV):
            op_token = self.current_token
            self.advance() 
            right = self.factor()
            opTree = OperationNode(left, op_token, right)
        return opTree
    
        ''' Check if the left is a factor[ call factor method for this]
    • Check if operator token is RR_MUL or RR_DIV
    • Check if the right is a factor[ call factor method for this]
    • [ recurrent checking can be done using a loop- that is for your HW]
    • If yes , advance
    • and return the operation node (class variable)
    Expression method uses similar code with PLUS|MINUS operations'''

    def expression(self):
        left = self.term()
        opTree = self.term()
        while self.current_token.type in (lex.BC_PLUS, lex.BC_MINUS):
            op_token = self.current_token
            self.advance()
            right = self.term()
            opTree = OperationNode(left, op_token, right)
        return opTree