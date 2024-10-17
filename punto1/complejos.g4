grammar complejos;

program: expr EOF;

expr: expr '+' term
    | expr '-' term
    | term
    ;

term: factor;

factor: '(' expr ')'
      | complexNumber
      | NUMBER
      ;

complexNumber: NUMBER? ('+'|'-')? NUMBER 'i';  // Imaginarios

NUMBER: [0-9]+ ('.' [0-9]+)?;  // Reales

WS: [ \t\r\n]+ -> skip; // Espacios en blanco