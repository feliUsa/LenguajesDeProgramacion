%{
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
double vbltable[26];
%}

%union{
    double dval;
    int vblno;
}

%token <vblno> NAME 
%token <dval> NUMBER
%left '-' '+'
%left '*' '/'
%nonassoc UNIMUS

%type <dval> expression

%%
statement_list: statement '\n'
    |   statement_list statement '\n'
    ;

statement: NAME '=' expression { vbltable[$1] = $3; }
    | expression { printf("= %g\n", $1); }
    ;

expression: expression '+' expression { $$ = $1 + $3; }
    | expression '-' expression { $$ = $1 - $3; }
    | expression '*' expression { $$ = $1 * $3; }
    | expression '/' expression
        { if($3 == 0) {
            yyerror("divide by zero");
            exit(EXIT_FAILURE);
          } else {
            $$ = $1 / $3;
          }
        }
    | '-' expression %prec UNIMUS { $$ = -$2; }
    | '(' expression ')' { $$ = $2; }
    | '|' expression '|' { $$ = fabs($2); }
    | NUMBER { $$ = $1; }
    | NAME { $$ = vbltable[$1]; }
    ;
%%
extern FILE *yyin;

int main()
{
    yyparse();
}

void yyerror(char *s)
{
    fprintf(stderr, "Syntax error: %s\n", s);
    exit(EXIT_FAILURE);
}
