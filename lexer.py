import error as errors
BC_INT = 'BC_INT'
BC_FLOAT = 'BC_FLOAT'
BC_PLUS = 'BC_PLUS'
BC_MINUS = 'BC_MINUS'
BC_MULT = 'BC_MULT'
BC_DIV = 'BC_DIV'
BC_PARENTH = 'BC_PARENTH'
DIGITS = "0123456789"

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens() 
    return tokens, error

'''Modify the run method
• # To generate Abstract Syntax Tree (AST)
parser = Parser(tokens) #tokens are output of lexer
AST= parser.parse()
return AST,None'''


class Token:
    def __init__(self, value, token_type):
        self.value = value
        self.type = token_type

    def __str__(self):
        return f"{self.type}:{self.value}"


class Lexer:
    def __init__(self, fn, text):
        self.fn = fn    
        self.text = text
        self.position = 0
        self.current_char = self.text[self.position] if self.position <= len(self.text) else None


    def advance(self):
        self.position += 1
        if self.position < len(self.text):
            self.current_char = self.text[self.position]
        else:
            self.current_char = None

    def make_digit(self):
        dot_count=0
        dig_str=""
        digit_type=BC_INT

        while self.current_char !=None and self.current_char in DIGITS+'.':
            if self.current_char=='.':
                dot_count+=1
                digit_type=BC_FLOAT
            if dot_count>1: digit_type="UNKNOWN"
            dig_str = dig_str + self.current_char
            self.advance()

        token = Token(dig_str,digit_type)
        return token
        
  
    def make_tokens(self):
        tokens = []
        error = None
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
                continue
            elif self.current_char == '+':
                tokens.append(str(Token(self.current_char, BC_PLUS)))
                self.advance()
            elif self.current_char == '-':
                tokens.append(str(Token(self.current_char, BC_MINUS)))
                self.advance()
            elif self.current_char == '*':
                tokens.append(str(Token(self.current_char, BC_MULT)))
                self.advance()
            elif (self.current_char == '(' or self.current_char == ')'):
                tokens.append(str(Token(self.current_char, BC_PARENTH)))
                self.advance()
            elif self.current_char == '/':
                tokens.append(str(Token(self.current_char, BC_DIV)))
                self.advance()
            elif self.current_char in DIGITS+'.':
                tokens.append(str(self.make_digit()))
            else:
                char = self.current_char
                self.advance()   
                '''line is hard coded for now, but will figure it out once we get file input going and there are multiple lines'''
                error = IllegalCharError( "'" + char + "' \nFile: " +  self.fn + ", Line 1 \nColumn:" + str(self.position) )
                 
        return tokens, error


class Error:

  def __init__(self, error_name, details):
    self.error_name = error_name
    self.details = details
  def as_string(self):
    result = f'{self.error_name}: {self.details}\n'
    return result

class IllegalCharError(Error):
  def __init__(self, details):
    super().__init__('Illegal Character', details)

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
            __________  //move to next
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