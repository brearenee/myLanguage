class NumberNode ():
    def __init__(self, token):
        self.token = token
    def __str__(self):
        return f"{self.token}"
    ##Constructor to initalize class variable token. 
    ##representation method to print in string format. 

class OperationNode():

    def __init (self, left_node, operator_token, right_node):
            self.left_node = left_node
            self.operator_token = operator_token
            self.right_node = right_node 
    def __str__(self):
        return f"left : {self.left_node} , token: {self.operator_token}, right: {self.right_node}"

    ##Constructor to initialize class variables. 
    ##??
    ##customer representation method to print instring format.

class Parser():
    def __init__(self, tokens):   
       ## self.position = 0
        self.tokens = tokens
        self.tokenIndex = 0
        self.current_token = tokens[tokenIndex]

        '''   Tokens //class variables
        • Token index// class variables 
    • Advance method to read (return) tokens if inside the text length '''

    def parse(self):
        result = self.expr()
        return result

    def advance(self): 
        self.tokenIndex += 1
        if self.self_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        else:
            self.current_token = None
     
    def factor(self):
        token = self.current_token
        if token.type in (BC_INT, BC_FLOAT):
            advance()
        return NumberNode(token)

    '''    Get the current token from the lexer output
    • Check if its RR_INT or RR_FLOAT
    • If yes , advance to next token
    • and return the number node (class variable)'''

    def term(self):
        left = factor()
        while self.current_tok.type in (_____, _______):
            op_token = self.current_token
          ##  __________  //move to next
            right = _________
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
    left = term()
    while self.current_tok.type in (_____, _______):
      op_token = self.current_token
      __________  //move to next
      right = _________
      opTree = OperationNode(left, op_token, right)
    return opTree