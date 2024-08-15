%{
#include <stdio.h>

#define NUMBER 258
#define ADD 259
#define SUB 260
#define MUL 261
#define DIV 262
#define ABS 263
#define EOL 264

void printToken(int token, const char* value) {
    if (value) {
        printf("%d = %s\n", token, value);
    } else {
        printf("%d\n", token);
    }
}
%}

%%

[0-9]+            { printToken(NUMBER, yytext); }

\+                { printToken(ADD, NULL); }
\-                { printToken(SUB, NULL); }
\*                { printToken(MUL, NULL); }
\/                { printToken(DIV, NULL); }

\|                { printToken(ABS, NULL); }

\n                { printToken(EOL, NULL); }

[ \t]             { /* Ignorar */ }

.                 { printf("%s = token no reconocible\n", yytext); }
%%

int main() {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
