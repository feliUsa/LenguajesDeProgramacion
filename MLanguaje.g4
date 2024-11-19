grammar MLanguaje;

program
    : statement* EOF
    ;

statement
    : varDeclaration
    | ifStatement
    | whileStatement
    | forStatement
    | methodCall
    | functionDecl
    | plotOperation
    | 'print' '(' expression ')'
    | fileOperation
    | mlFunction
    | matrixOperation
    ;

varDeclaration
    : 'let' ID '=' expression
    ;

functionDecl
    : 'def' ID '(' paramList? ')' '{' statement* '}'
    ;

paramList
    : ID (',' ID)*
    ;

ifStatement
    : 'if' '(' expression ')' '{' statement* '}' ('else' '{' statement* '}')?
    ;

whileStatement
    : 'while' '(' expression ')' '{' statement* '}'
    ;

forStatement
    : 'for' '(' varDeclaration ';' expression ';' expression ')' '{' statement* '}'
    ;

methodCall
    : ID '.' ID '(' (expression (',' expression)*)? ')'
    ;

fileOperation
    : 'readFile' '(' STRING ')'
    | 'writeFile' '(' STRING ',' STRING ')'
    | 'readCSV' '(' STRING ')'
    | 'writeCSV' '(' STRING ',' expression ')'
    ;

plotOperation
    : 'plotLine' '(' expression ',' expression ')' # PlotLine
    | 'plotBar' '(' expression ',' expression ')'  # PlotBar
    ;

mlFunction
    : 'multilayer_perceptron' '(' expression ',' expression (',' expression (',' expression)?)? ')'
    | 'kmeans_clustering' '(' expression ',' expression (',' expression)? ')'
    ;

matrixOperation
    : expression '.' ('add' | 'subtract' | 'multiply' | 'transpose' | 'inverse') '(' expression? ')'
    ;

expression
    : expression ('+' | '-' | '*' | '/' | '%' | '^') expression
    | expression ('>' | '<' | '>=' | '<=' | '==' | '!=') expression
    | '(' expression ')'
    | '-'? NUMBER
    | STRING
    | ID
    | list
    | matrixConstructor
    | methodCall
    | '-'? NUMBER
    | 'true'
    | 'false'
    | ID '.' 'transpose' '(' ')'
    | ID '.' 'inverse' '(' ')'
    | 'sin' '(' expression ')'
    | 'cos' '(' expression ')'
    | 'tan' '(' expression ')'
    ;

list
    : '[' (expression (',' expression)*)? ']'
    ;

matrixConstructor
    : 'matrix' '(' list ')'
    ;

ID
    : [a-zA-Z_] [a-zA-Z_0-9]*
    ;

NUMBER
    : [0-9]+ ('.' [0-9]+)?
    ;

STRING
    : '"' (~["\\] | '\\' .)* '"'
    ;

WHITESPACE
    : [ \t\r\n]+ -> skip
    ;

COMMENT
    : '#' ~[\r\n]* -> skip
    ;
