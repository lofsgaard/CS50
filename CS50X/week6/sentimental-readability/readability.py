# TODO
from cs50 import get_string
import re


def main():
    text = get_string("Text: ")
    calc_readability(text)


def calc_readability(s):
    words = s.split(' ')
    sentence = re.split('[.!?]', s)
    nr_letters = 0
    for x in s:
        if x.isalpha():
            nr_letters += 1
    nr_words = len(words)
    nr_sentence = len(sentence) - 1

    avg_letters = nr_letters / nr_words * 100
    avg_sentences = nr_sentence / nr_words * 100

    readability = round(0.0588 * round(avg_letters, 2) - 0.296 * round(avg_sentences, 2) - 15.8)
    if int(readability) < 0:
        print("Before Grade 1")
    elif int(readability) >= 16:
        print("Grade 16+")
    else:
        print(f'Grade {readability}')


if __name__ == "__main__":
    main()
