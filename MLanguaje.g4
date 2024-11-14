grammar MLanguaje;

program
    : (statement | functionDecl)* EOF
    ;

statement
    : varDeclaration                   # DeclareVarStmt
    | expression                       # ExprStmt
    | ifStatement                      # IfStmt
    | whileStatement                   # WhileStmt
    | forStatement                     # ForStmt
    | fileOperation                    # FileOpStmt
    | plotOperation                    # PlotOpStmt
    ;

varDeclaration
    : LET? ID '=' expression
    ;

functionDecl
    : 'def' ID '(' parameterList? ')' '{' program '}'
    ;

parameterList
    : ID (COMMA ID)*
    ;

list
    : '[' (expression (COMMA expression)*)? ']'
    ;

comparison
    : expression ('>' | '<' | '==' | '!=' | '>=' | '<=') expression
    ;

ifStatement
    : 'if' '(' comparison ')' '{' program '}' ('else' '{' program '}')?
    ;

whileStatement
    : 'while' '(' comparison ')' '{' program '}'
    ;

forStatement
    : 'for' '(' varDeclaration ';' comparison ';' expression ')' '{' program '}'
    ;

expression
    : primaryExpression                                   # PrimaryExpr
    ;

primaryExpression
    : primaryExpression '^' primaryExpression             # PowerExpr
    | primaryExpression ('*' | '/' | '%') primaryExpression  # MultExpr
    | primaryExpression ('+' | '-') primaryExpression       # AddExpr
    | '(' expression ')'                                  # ParenExpr
    | functionCall                                        # CallFunc
    | trigFunction                                        # TrigFunc
    | list                                                # ListExpr
    | ID                                                  # VarExpr
    | NUMBER                                              # NumberExpr
    | STRING                                              # StringExpr
    | 'true'                                              # TrueExpr
    | 'false'                                             # FalseExpr
    ;

matrixOperation
    : ID '.' (ADD | SUBTRACT | MULTIPLY | TRANSPOSE | INVERSE) '(' (expression (COMMA expression)*)? ')'
    ;

fileOperation
    : READ_FILE LPAREN STRING (COMMA expression)? RPAREN
    ;

plotOperation
    : PLOT_LINE LPAREN expression (COMMA expression)* RPAREN
    ;

functionCall
    : ID LPAREN argumentList? RPAREN
    ;

argumentList
    : expression (COMMA expression)*
    ;

trigFunction
    : (SIN | COS | TAN) LPAREN expression RPAREN
    ;

LET: 'let';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+('.'[0-9]+)?;
STRING: '"' .*? '"';
COMMA: ',';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
READ_FILE: 'readFile';
WRITE_FILE: 'writeFile';
PLOT_LINE: 'plotLine';
PLOT_BAR: 'plotBar';
SIN: 'sin';
COS: 'cos';
TAN: 'tan';
TRUE: 'true';
FALSE: 'false';
WS: [ \t\r\n]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;
ADD: 'add';
SUBTRACT: 'subtract';
MULTIPLY: 'multiply';
TRANSPOSE: 'transpose';
INVERSE: 'inverse';
