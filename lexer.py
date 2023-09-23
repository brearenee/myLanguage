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

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens() 
    if error: return error
    else: 
        parser = p.Parser(tokens) #tokens are output of lexer
        AST= parser.parse()
        return AST, None

class Token:
    def __init__(self, token_type, value=None ):
        self.value = value
        self.type = token_type

    def __str__(self):
        if self.value is None:
            return f"{self.type}"
        else:
            return f"{self.type}:{self.value}"

class Lexer:
    def __init__(self, fn, text):
        self.linenum = 1
        self.fn = fn    
        self.text = text
        self.position = 0
        self.current_char = text[0]
        self.pos = Position(self.position, self.linenum, self.position, self.fn, self.text)

    def advance(self):
        self.position += 1
        if self.position < len(self.text):
            self.current_char = self.text[self.position]
            self.pos = Position(self.position, self.linenum, self.position, self.fn, self.text)
        else:
            self.current_char = None
            self.pos = Position(-1, self.linenum, self.position, self.fn, self.text)


    def make_digit(self):
        dot_count=0
        dig_str=""
        digit_type=BC_INT

        while self.current_char is not None and self.current_char in DIGITS+'.':
            if self.current_char=='.':
                dot_count+=1
                digit_type=BC_FLOAT
            if dot_count>1: digit_type="UNKNOWN"
            dig_str = dig_str + self.current_char
            self.advance()

        token = Token(digit_type,dig_str)
        return token

    def make_tokens(self):
        tokens = []
        error = None

        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
                continue
            elif self.current_char == '+':
                tokens.append(Token(BC_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token( BC_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(BC_MULT))
                self.advance()
            elif (self.current_char == '('):
                tokens.append(Token(BC_L_PAR))
                self.advance()
            elif (self.current_char == ')'):
                tokens.append(Token(BC_R_PAR))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(BC_DIV))
                self.advance()
            elif self.current_char in DIGITS+'.':
                tokens.append(self.make_digit())
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
        if self.sindex == -1:
            self.char = "None"
        else: self.char = text[sindex]

    def __str__(self):
        return "'" + self.char + "' \nFile: " +  self.fn + ", Line 1 \nColumn:" + str(self.col_num) 
