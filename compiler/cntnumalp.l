/* Program 2 Identify Input Text is digit or string. */
%{
%}

digit   [0-9]+
string  [a-zA-Z]+

%%
{digit}     printf("Digit: %s\n", yytext);
{string}    printf("String: %s\n", yytext);
%%

int yywrap()
{
    return 1;
}

int main()
{
    yylex();
    return 0;
}