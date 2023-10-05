import lexer as lexer
import errors as error
import parse as parser

while True:
    
     text = input('B@C > ')
     result, error = lexer.run('<stdin>', text)
     if error:
          print("error printing")
          print(error)
     else: print(result)
     
'''
    try:
          text = input('B@C > ')
          result, error = lexer.run('<stdin>', text)
          if error:
               print("error prining")
               ##print(error.as_string())
          else: print(result)
    except SyntaxError as e:
       print(e.details)'''

