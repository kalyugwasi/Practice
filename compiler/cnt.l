/* Program 6 Count and Identify Tokens */
%option noyywrap

%{
#include <stdio.h>
int n = 0;
%}

%%
while|if|else {
    n++;
    printf("Keyword: %s\n", yytext);
}

int|float|double {
    n++;
    printf("Keyword: %s\n", yytext);
}

[a-zA-Z_][a-zA-Z0-9_]* {
    n++;
    printf("Identifier: %s\n", yytext);
}

"<="|"=="|"++"|"+"|"*"|"-" {
    n++;
    printf("Operator: %s\n", yytext);
}

[(){};,<>=/.] {
    n++;
    printf("Separator: %s\n", yytext);
}

[0-9]+\.[0-9]+ {
    n++;
    printf("Float Constant: %s\n", yytext);
}

[0-9]+ {
    n++;
    printf("Integer Constant: %s\n", yytext);
}

[ \t\n]+   ;
%%

int main(void)
{
    yylex();
    printf("Total Tokens = %d\n", n);
    return 0;
}