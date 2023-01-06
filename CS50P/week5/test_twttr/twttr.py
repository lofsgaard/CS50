def main():
    print(shorten(input("Input: ")))


def shorten(word):
    table = str.maketrans(dict.fromkeys('aeiouAEIOU'))
    return word.translate(table)

if __name__ == "__main__":
    main()
