grammar MLanguaje;

program: (statement | NEWLINE)* EOF;

statement
    : variableDeclaration
    | printStatement
    | ifStatement
    | whileLoop
    | forLoop
    | expressionStatement
    | matrixOperation
    | fileOperation
    | visualization
    | NEWLINE
    ;

variableDeclaration: 'let' ID '=' expression (NEWLINE | EOF);

printStatement: 'print' '(' (STRING | expression) ')' (NEWLINE | EOF);

ifStatement
    : 'if' '(' condition ')' '{' statement* '}' ('else' '{' statement* '}')?
    ;

whileLoop: 'while' '(' condition ')' '{' statement+ '}';

forLoop: 'for' ID 'in' (expression) '{' statement* '}';

list_: '[' expression (',' expression)* ']' NEWLINE?;


expressionStatement: expression (NEWLINE | EOF);

expression
    : expression ('+' | '-' | '*' | '/' | '**') expression
    | 'sin' '(' expression ')'
    | 'cos' '(' expression ')'
    | 'power' '(' expression ',' expression ')'
    | 'sqrt' '(' expression ')'
    | list_
    | rangeExpr  // Añadido aquí para soportar rangos como expresiones
    | matrixOperation
    | fileOperation
    | INT
    | FLOAT
    | ID
    | STRING
    ;


matrixOperation
    : 'addMatrix' '(' expression ',' expression ')'
    | 'multiplyMatrix' '(' expression ',' expression ')'
    | 'transposeMatrix' '(' expression ')'
    | 'inverseMatrix' '(' expression ')'
    | 'linearRegressionFit' '(' expression ',' expression ')'
    | 'linearRegressionPredict' '(' expression ',' expression ')'
    | 'mlpFit' '(' expression ',' expression (',' expression (',' expression)?)? ')'
    | 'mlpPredict' '(' expression ',' expression ')'
    ;


fileOperation
    : 'writeFile' '(' STRING ',' STRING ')'
    | 'readFile' '(' STRING ')'
    | 'writeCSV' '(' STRING ',' expression ')'
    | 'readCSV' '(' STRING ')'
    | 'loadCSV' '(' STRING ')'; // Asegúrate de que esta línea esté presente


visualization
    : plotLine
    | plotBar
    | plotHistogram
    | plotScatter3D
    ;

plotLine: 'plotLine' '(' expression ',' expression ')';
plotBar: 'plotBar' '(' expression ',' expression ')';
plotHistogram: 'plotHistogram' '(' expression ')';
plotScatter3D: 'plotScatter3D' '(' expression ',' expression ',' expression ')';

condition
    : expression ('>' | '<' | '==' | '!=' | '>=' | '<=') expression
    ;

rangeExpr: 'range' '(' INT (',' INT)? ')';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' .*? '"';
INT: [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip;
LINE_COMMENT: '#' ~[\r\n]* -> skip;