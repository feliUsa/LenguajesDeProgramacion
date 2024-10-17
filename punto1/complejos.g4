grammar complejos;

program: expr EOF;

expr: expr '+' term   # Add
    | expr '-' term   # Subtract
    | term            # SingleTerm
    ;

term: factor;

factor: '(' expr ')'   # Parentheses
      | complexNumber  # ComplexExpr
      | NUMBER         # RealNumber
      ;

complexNumber: NUMBER? ('+'|'-')? NUMBER 'i';  // Imaginarios

NUMBER: [0-9]+ ('.' [0-9]+)?;  // Reales

WS: [ \t\r\n]+ -> skip; // Espacios en blanco