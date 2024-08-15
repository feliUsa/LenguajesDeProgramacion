%{
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int num_lines = 0;    // Contador de líneas
int num_words = 0;    // Contador de palabras
int num_chars = 0;    // Contador de caracteres

%}

%%

\n              { num_lines++; }
[ \t]+          { /* Ignorar espacios y tabulaciones */ }
[0-9]+          { num_chars++; }
-?+             { num_chars++; }
[A-Za-z]+       { num_lines++; num_chars += strlen(yytext); num_words++;}
.               { num_chars++; }

%%

int main(int argc, char **argv) {
    yylex();
    printf("Número total de caracteres: %d\n", num_chars);
    printf("Número de palabras: %d\n", num_words);
    printf("Número de líneas: %d\n", num_lines);
    return 0;
}