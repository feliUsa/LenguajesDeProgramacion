grammar transformadas;

program: expr EOF;

expr: 'fourier(' array ',' NUMBER ')'           # FourierTransform
    | 'inversa(' array ',' NUMBER ')'           # InverseFourierTransform
    | 'pulsoRectangular(' NUMBER ')'            # PulsoRectangular
    | 'pulsoTriangular(' NUMBER ')'             # PulsoTriangular
    | 'signum()'                                # Signum
    | 'deltaDirac()'                            # DeltaDirac
    | 'cos(' NUMBER ')'                         # Cos
    | 'sin(' NUMBER ')'                         # Sin;

array: '[' elements ']'                         # ArrayExpr;

elements: complexNumber (',' complexNumber)*;   // Lista de números complejos separados por comas

// Definir correctamente un número complejo, soportando números negativos
complexNumber: realPart imaginaryPart?;

realPart: ('-' | '+')? NUMBER;   // Parte real opcional (puede ser positiva o negativa)

imaginaryPart: ('+' | '-') NUMBER 'i';  // Parte imaginaria con signo

NUMBER: [0-9]+ ('.' [0-9]+)?;          // Números enteros o decimales

WS: [ \t\r\n]+ -> skip;                // Ignorar espacios en blanco
