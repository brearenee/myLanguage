Notes for assignment. 



parser: a program that generates a parse tree for a given string, if the string is generates from underlying grammar. 

TODO: Complete the parser program that will work for simple arithmetic expressions like 1+2*4  and submit the program and the output screenshot.


GRAMMAR: 

expr : term ((PLUS|MINUS) term)*
term : factor ((MUL|DIV) factor)*
factor : INT|FLOAT


OUTPUT: 
1 + 2 * 3  should output 
(INT: 1, PLUS, (INT: 2, MUL, INT:3))