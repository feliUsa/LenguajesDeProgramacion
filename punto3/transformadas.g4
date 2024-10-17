grammar transformadas;

program: expr EOF;

expr: 'fourier(' array ',' NUMBER ')' # FourierTransform
    | 'inversa(' array ',' NUMBER ')' # InverseFourierTransform;

array: '[' elements ']'  # ArrayExpr;

elements: complexNumber (',' complexNumber)*;  // Lista de números complejos separados por comas

complexNumber: NUMBER ('+' | '-') NUMBER 'i'?;  // Definir un número complejo

NUMBER: [0-9]+ ('.' [0-9]+)?;  // Números enteros o decimales

WS: [ \t\r\n]+ -> skip;  // Ignorar espacios en blanco
