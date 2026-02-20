/* Program 5 To check if Characters other than alphabets in a string */
%option noyywrap
%{
%}

%%
[a-zA-Z]+ {	printf("No Character other than alphabets");}
.*	{	printf("Character other than alphabets Present");}
%%
int main()
{
	yylex();
	return 0;
}