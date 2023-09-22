import lexer as lexer
import parse as parser

while True:
    text = input('B@C> ')
    result = lexer.run('<stdin>', text)
    ##print("results:")
   ## if error: print(error.as_string())
   ## else:
 
    for i in result:
            print(str(i))


