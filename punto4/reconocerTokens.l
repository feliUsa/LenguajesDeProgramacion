%{
#include <stdio.h>

#define NUMBER 258
#define ADD 259
#define SUB 260
#define MUL 261
#define DIV 262
#define ABS 263
#define EOL 264
%}

%%

[0-9]+            { printf("NUMBER (%d) --> %s\n", NUMBER, yytext); }
\+                { printf("ADD (%d) --> %s\n", ADD, yytext); }
\-                { printf("SUB (%d) --> %s\n", SUB, yytext); }
\*                { printf("MUL (%d) --> %s\n", MUL, yytext); }
\/                { printf("DIV (%d) --> %s\n", DIV, yytext); }
\|                { printf("ABS (%d) --> %s\n", ABS, yytext); }
\n                { printf("EOL (%d) --> %s\n", EOL, yytext); }
[ \t]             { /* Ignorar */ }
.                 { printf("%s : Token no reconocible\n", yytext); }

%%

int main() {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
