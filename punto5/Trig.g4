grammar Trig;

prog:   expr+ ;

expr:   trigFunc '(' NUMBER ')' ;

trigFunc: 'Sin' | 'Cos' | 'Tan' ;

NUMBER: [0-9]+('.'[0-9]+)? ;
WS:     [ \t\r\n]+ -> skip ;
