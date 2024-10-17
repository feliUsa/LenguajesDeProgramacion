grammar appFuncion;

program: statement+ EOF;

statement: mapFunction
         | filterFunction;

mapFunction: 'MAP' '(' function ',' iterable ')';
filterFunction: 'FILTER' '(' condition ',' iterable ')';

function: IDENTIFIER;
condition: IDENTIFIER;

iterable: IDENTIFIER;

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;
