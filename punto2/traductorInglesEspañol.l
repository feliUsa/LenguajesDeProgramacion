%{
#include <stdio.h>
%}

%%

español          { printf("spanish "); }
ingles           { printf("english "); }
desde            { printf("from "); }
porque           { printf("why "); }
hasta            { printf("until "); }
celular          { printf("celphone "); }
computador       { printf("computer "); }
tiene            { printf("have "); }
hacer            { printf("do "); }
puede            { printf("can "); }
hola             { printf("hello "); }
adios            { printf("bye "); }
vida             { printf("life "); }
lenguaje         { printf("languaje "); }
programacion     { printf("programming "); }


spanish          { printf("español "); }
english          { printf("ingles "); }
from             { printf("desde "); }
why              { printf("porque "); }
until            { printf("hasta "); }
celphone         { printf("celular "); }
computer         { printf("computador "); }
have             { printf("tiene "); }
do               { printf("hacer "); }
can              { printf("puede "); }
hello            { printf("hola "); }
bye              { printf("adios "); }
life             { printf("vida "); }
languaje         { printf("lenguaje "); }
programming      { printf("programacion "); }

[ \t\n]          { /* Ignorar espacios, tabulaciones y nuevas líneas */ }
.                { printf("%s ", yytext); } /* Si no reconoce la palabra, no se traduce */

%%

/* Código C adicional */
int main() {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
