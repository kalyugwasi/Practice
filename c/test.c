#include <stdio.h>
#include <ctype.h>

int countTokens(char *fname)
{
    FILE *fp;
    char ch;
    int tokens = 0;

    fp = fopen(fname, "r");
    if (fp == NULL)
    {
        printf("Cannot open %s\n", fname);
        return 0;
    }

    while ((ch = fgetc(fp)) != EOF)
    {
        if (isalnum(ch) || ch == '_')
        {
            tokens++;
            while (isalnum(ch) || ch == '_')
                ch = fgetc(fp);
        }
        else if (ch == '"')
        {
            tokens++;
            while ((ch = fgetc(fp)) != '"');
        }
        else if (!isspace(ch))
        {
            tokens++;
        }
    }

    fclose(fp);
    return tokens;
}

int main()
{
    int t1, t2;
    t1 = countTokens("source1.c");
    t2 = countTokens("source2.c");

    printf("Tokens in source1.c = %d\n", t1);
    printf("Tokens in source2.c = %d\n", t2);

    return 0;
}
