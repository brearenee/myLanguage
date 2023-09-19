import lexer as lexer
import error as errors

while True:
    text = input('B@C> ')
    result, error = lexer.run('<stdin>', text)
    print("results:")
    if error: print(error.as_string())
    else:
        print(result)

