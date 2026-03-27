%option noyywrap
%{
#include <stdio.h>
int positive_no = 0,negative_no = 0;
%}
%%
-[0-9]+ {
    negative_no++;
    printf("Negative Number = %s\n",yytext);
}
[0-9]+ {
    positive_no++;
    printf("Positive Numbers = %s\n",yytext);
}
[\t\n]+;
%%
int main(void)
{
    yylex();
    printf("\nNumbers of Positive Numbers = %d",positive_no);
    printf("\nPositive of Negative Number = %d",negative_no);
    return 0;
}