

## Parse Tree Rules: 
•start with empty node.
•If the current token is a "(", add a new node as the left child of the current node,
and descend to that left child.
• If the current token is in the list ["+", "-", "/", "*"], set the root value of the current
node to the operator represented by the current token. Add a new node as the
right child of the current node and descend to that right child.
• If the current token is a number, set the root value of the current node to the
number and return to the parent.
• If the current token is a ")", go to the parent of the current node

user input inserted. 
we call the *run* method inside lexor file. 

the *run* method creates a *lexor object* with the user input. 
Everything is initalized via construtor.  

it uses that new instance of the *lexor object* to call *make_token()*s. 

*make_tokens()* take the entire input (self.text) and goes through to check each character.
for each character (space + - ...etc) it creates a *Token object*. 

This *Token object* just has info about its self and type.  

if *make_tokens()* runs across a digit, it calls *make_digit()*. This function will take the whole number(556) instead of just each charcater by utilizing the *"self.position"* value and the *"advance()"*  method of the *Lexor Object.*  
if it runs into a . , it knows the token is a float not an int. 
if it has more than one ., it does throw an error yet, but just lists its type as "unknown"

once *make_tokens* is complete, it returns the list of *Token objects* back to the *run* method.  This returns the list back to main for printing. 




