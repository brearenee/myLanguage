## myLanguage
project for Principles of Prigramming Language, MSU Denver Fall 2022. 



**DONE:**   
***Part 1***  
- the program now recognizes tokens from user input.   These tokens can be integers/floats or various operators.  It throws an error if an alphabetical/unknown character is imputted.  It outputs the token in format ["token name" : "token value (if digit)"]

**TODO:**  
***lab 04, prep for part2:***  
- Create a parser for tokens.  This parser will generate a parse tree for a given string, if the string is generated from underlying grammar.  

- Complete the parser program that will work for simple arithmetic expressions like 1+2*4  and submit the program and the output screenshot.


GRAMMAR: 

expr : term ((PLUS|MINUS) term)*
term : factor ((MUL|DIV) factor)*
factor : INT|FLOAT

INPUT: 1+2*4  
OUTPUT: 
1 + 2 * 3  should output 
(INT: 1, PLUS, (INT: 2, MUL, INT:3))