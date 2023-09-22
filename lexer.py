import errors as errors
import parse as p

BC_INT = 'BC_INT'
BC_FLOAT = 'BC_FLOAT'
BC_PLUS = 'BC_PLUS'
BC_MINUS = 'BC_MINUS'
BC_MULT = 'BC_MULT'
BC_DIV = 'BC_DIV'
BC_L_PAR = 'BC_L_PARENTH'
BC_R_PAR = 'BC_R_PARENTH'
DIGITS = "0123456789"

operator_list = [BC_PLUS, BC_MINUS, BC_MULT, BC_DIV, BC_L_PAR, BC_R_PAR ]

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens() 
    ##return tokens, error
    # To generate Abstract Syntax Tree (AST)
    parser = p.Parser(tokens) #tokens are output of lexer
    AST= parser.parse()
    print("do i reach this in run? \n")
    return AST, error, None

class Token:
    def __init__(self, value, token_type):
        self.value = value
        self.type = token_type

    def __str__(self):
        if self.type in operator_list:
            return f"{self.type}"
        else:
            return f"{self.type}:{self.value}"

class Lexer:
    def __init__(self, fn, text):
        self.linenum = 1
        self.fn = fn    
        self.text = text
        self.position = 0
        self.current_char = self.text[self.position] if self.position <= len(self.text) else None
        self.pos = Position(self.position, self.linenum, self.position, self.fn, self.text)

    def advance(self):
        self.position += 1
        if self.position < len(self.text):
            self.current_char = self.text[self.position]
            self.pos = Position(self.position, self.linenum, self.position, self.fn, self.text)
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
            elif (self.current_char == '('):
                tokens.append(str(Token(self.current_char, BC_L_PAR)))
                self.advance()
            elif (self.current_char == ')'):
                tokens.append(str(Token(self.current_char, BC_R_PAR)))
                self.advance()
            elif self.current_char == '/':
                tokens.append(str(Token(self.current_char, BC_DIV)))
                self.advance()
            elif self.current_char in DIGITS+'.':
                tokens.append(str(self.make_digit()))
            else: 
                char = self.current_char
                error = errors.IllegalCharError( self.pos )
                self.advance()
         
        return tokens, error

class Position: 
    def __init__(self, sindex, linenum, columnnumber, fn, text):
        self.sindex = sindex
        self.line_num = linenum
        self.col_num = columnnumber + 1
        self.fn = fn
        self.text = text
        self.char = text[sindex]

    def __str__(self):
        return "'" + self.char + "' \nFile: " +  self.fn + ", Line 1 \nColumn:" + str(self.col_num) 
