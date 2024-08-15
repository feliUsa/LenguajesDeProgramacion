%{
/* Código en C para incluir las librerías necesarias */
#include <stdio.h>
%}

%%



[0-9]+(\.[0-9]+)?    { printf("Número: %s\n", yytext); }


"+"                  { printf("Operación: Suma (+)\n"); }
"-"                  { printf("Operación: Resta (-)\n"); }
"*"                  { printf("Operación: Multiplicación (*)\n"); }
"/"                  { printf("Operación: División (/)\n"); }
"="                  { printf("Operación: Igual (=)\n"); }
"^"                  { printf("Operación: Potencia (^)\n"); }


[a-zA-Z]             { printf("Caracter: %s\n", yytext); }


[ \t\n]              { /* Ignorar */ }

.                    { printf("Símbolo no reconocido: %s\n", yytext); }
%%


int main() {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
