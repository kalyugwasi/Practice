%option noyywrap
%{
#include <stdio.h>
int count = 0;
%}
%%
[a-zA-Z0-9]+   { count++; }
%%
int main()
{
    FILE *fp = fopen("hello.txt", "r");
    if (!fp)
    {
        printf("Cannot open file\n");
        return 1;
    }

    yyin = fp;
    yylex();
    printf("Total Words: %d\n", count);
    fclose(fp);
    return 0;
}