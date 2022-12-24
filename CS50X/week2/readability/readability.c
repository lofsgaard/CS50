#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("text: ");
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);
    float L = (float)letters / words * 100.0;
    float S = (float)sentences / words * 100.0;

    float index = 0.0588 * L - 0.296 * S - 15.8;
    if (index >= 1 && index <= 16)
    {
        printf("Grade %i\n", (int) round(index));
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index <= 0)
    {
        printf("Before Grade 1\n");
    }
}

int count_sentences(string text)
{
    int periods = 0;
    for (int i = 0; text[i] != '\0'; i++)
    {

        if (text[i] == 33 || text[i] == 46 || text[i] == 63)
        {

            periods++;
        }
    }
    return periods;
}


int count_words(string text)
{
    int spaces = 1;
    for (int i = 0; text[i] != '\0'; i++)
    {

        if (text[i] == ' ')
        {

            spaces++;
        }
    }
    return spaces;
}

int count_letters(string text)
{
    int length = strlen(text);
    int r = 0;

    for (int i = 0; i < length; i++)
    {
        if (islower(text[i]))
        {
            r++;
        }
        else if (isupper(text[i]))
        {
            r++;
        }
    }
    return r;
}