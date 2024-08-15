%{
#include <stdio.h>

/* Clasificacion de un numero complejo */
void printComplexNumber(const char* realPart, const char* imaginaryPart) {
    if (realPart && imaginaryPart) {
        printf("Número complejo: %s %s i\n", realPart, imaginaryPart);
    } else if (realPart) {
        printf("Número real: %s\n", realPart);
    } else if (imaginaryPart) {
        printf("Número imaginario: %s i\n", imaginaryPart);
    }
}
%}

%%


[+-]?[0-9]+(\.[0-9]+)?[ \t]*[+-][ \t]*[0-9]+(\.[0-9]+)?i {
    char realPart[100];
    char imaginaryPart[100];
    sscanf(yytext, "%s %s", realPart, imaginaryPart);
    printComplexNumber(realPart, imaginaryPart);
}


[+-]?[0-9]+(\.[0-9]+)?i {
    char imaginaryPart[100];
    sscanf(yytext, "%s", imaginaryPart);
    printComplexNumber(NULL, imaginaryPart);
}

[+-]?[0-9]+(\.[0-9]+)? {
    char realPart[100];
    sscanf(yytext, "%s", realPart);
    printComplexNumber(realPart, NULL);
}

[ \t\n]+ { /* Ignorar */ }

. { printf("Entrada no reconocida: %s\n", yytext); }
%%

int main() {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
