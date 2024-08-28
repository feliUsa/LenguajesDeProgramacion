grammar Calculator;

prog:   stat+ ;
stat:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   NEWLINE                     # blank
    ;
expr:   expr op=('*'|'/') expr      # MulDiv
    |   expr op=('+'|'-') expr      # AddSub
    |   INT                         # int
    |   ID                          # id
    |   '(' expr ')'                # parens
    ;
MUL :   '*' ; // Define the multiplication token
DIV :   '/' ; // Define the division token
ADD :   '+' ; // Define the addition token
SUB :   '-' ; // Define the subtraction token
ID  :   [a-zA-Z]+ ; // Define the ID token
INT :   [0-9]+ ; // Define the integer token
NEWLINE:'\r'? '\n' ; // Define the newline token
WS  :   [ \t]+ -> skip ; // Skip spaces and tabs
