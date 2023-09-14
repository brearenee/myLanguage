import error as errors
BC_INT = 'BC_INT'
BC_FLOAT = 'BC_FLOAT'
BC_PLUS = 'BC_PLUS'
BC_MINUS = 'BC_MINUS'
DIGITS = "0123456789"

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens() 
    return tokens, error


class Token:
    def __init__(self, value, token_type):
        self.value = value
        self.type = token_type

    def __str__(self):
        return f"[value:'{self.value}', type:'{self.type}']"

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
                tokens.append(str(Token(self.current_char,BC_MINUS,)))
                self.advance()
            elif self.current_char in DIGITS+'.':
                tokens.append(str(self.make_digit()))
            else:
                char = self.current_char
                self.advance()   
                error = IllegalCharError( "'" + char + "'")
                 
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