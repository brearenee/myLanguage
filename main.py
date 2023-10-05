import lexer as lexer
import errors as error
import parse as parser

while True:
    
     text = input('B@C > ')
     result, error = lexer.run('<stdin>', text)
     if error:
          print(error)
     else: print(result)
     
