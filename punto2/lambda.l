%{
#include <stdio.h>
int error = 0;
%}

%%
[ \t\n]+                   ;
"lambda"                   { /* Reconoce la palabra clave lambda */ } 
[a-zA-Z_][a-zA-Z0-9_]*     { /* Reconoce identificadores */ }
"="                        { /* Reconoce el signo de asignación */ }
":"                        { /* Reconoce los dos puntos */ }
[0-9]+                     { /* Reconoce números enteros */ }
\*\*                       { /* Reconoce el operador de exponenciación */ }
"\("                       { /* Reconoce el paréntesis de apertura */ }
"\)"                       { /* Reconoce el paréntesis de cierre */ }
.                          { error = 1; }
%%

int main(int argc, char **argv) {
    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            perror(argv[1]);
            return 1;
        }
    }
    yylex();

    if (error == 0) {
        printf("ACEPTA\n");
    } else {
        printf("NO ACEPTA\n");
    }
    
    return 0;
}

int yywrap() {
    return 1;
}
