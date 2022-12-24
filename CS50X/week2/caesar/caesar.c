#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>

bool only_digits(string s);
char rotate(char c, int n);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else if (!only_digits(argv[1]))
    {
        int k = atoi(argv[1]);
        string p = get_string("plaintext: ");
        printf("ciphertext: ");
        for (int i = 0, s = strlen(p); i < s; i++)
        {
            rotate(p[i], k);
        }
        printf("\n");
    }
    else if (only_digits(argv[1]))
    {
        return 1;
    }
}

bool only_digits(string s)
{
    for (int i = 0, len = strlen(s); i < len; i++)
    {
        if (!isdigit(s[i]))
        {
            return 1;
        }
    }
    return 0;
}


char rotate(char c, int n)
{

    if islower(c)
    {
        printf("%c", (((c + n) - 97) % 26) + 97);
    }
    else if isupper(c)
    {
        printf("%c", (((c + n) - 65) % 26) + 65);
    }

    else
    {
        printf("%c", c);
    }
    return 0;
}