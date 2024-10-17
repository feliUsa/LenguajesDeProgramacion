grammar transformadas;

program: expr EOF;

expr: 'fourier(' array ',' NUMBER ')' # FourierTransform;

array: '[' elements ']'  # ArrayExpr;

elements: NUMBER (',' NUMBER)*;  // Lista de números separados por comas

NUMBER: [0-9]+ ('.' [0-9]+)?;  // Números enteros o decimales

WS: [ \t\r\n]+ -> skip;  // Ignorar espacios en blanco